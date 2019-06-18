import os

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_dance.contrib.github import make_github_blueprint, github

from db import db
from resources.bookingmail import sendmail

app = Flask(__name__)

DBURL = 'mysql://root:vikash@localhost/resturantdb'

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # set OAuth lib to use insecure transport

blueprint = make_github_blueprint(client_id='439d53504eebbdf23d99',
                                  client_secret='c1d864c1ae8008123c8eecbee941a8436cbfdd6c')
app.register_blueprint(blueprint, url_prefix='/github_login')
app.config['SQLALCHEMY_DATABASE_URI'] = DBURL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mysecretkey'

from models.bookings import Resturant,Bookings


@app.route('/login')
def login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        return redirect('/')


@app.route('/')
def home():
    username = None
    if github.authorized:
        username = github.get('/user').json()['name']
    return render_template('homepage.html', username=username)


@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'GET':
        if not github.authorized:
            flash("You are not authorixed to access this page")
            return redirect('/')
        username = github.get('/user').json()['name']
        if username:
            resturants = db.session.query(Resturant.resturant_name).all()
            return render_template('home.html', resturants=resturants, user_name=username)
        return redirect(url_for('login'))
    if request.method == 'POST':
        username = request.form['user_name']
        resturant = request.form['resturant']
        phone = request.form['phone']
        email = request.form['email']
        no_of_seats = request.form['no_of_seats']
        message = f'Booking confirmed for today for {username} at {resturant} for {no_of_seats} people \n. We ' \
            f' will contact you on phone no: {phone} & email :{email} with further details.'
        sendmail(address=email, message=message)
        flash(message)
        # booking = Bookings(username,resturant,no_of_seats)
        # db.session.add(booking)
        # db.session.commit()
        return render_template('bookingconfirmation.html')


@app.route('/confirmation')
def confirmation():
    name = request.get()


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True, port=5000)
