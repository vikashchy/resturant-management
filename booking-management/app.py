from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from .config import DBURL
# from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
import flask_dance.consumer
from flask_dance.contrib.github import make_github_blueprint, github

import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # set OAuth lib to use insecure transport

blueprint = make_github_blueprint(client_id='439d53504eebbdf23d99',
                                  client_secret='c1d864c1ae8008123c8eecbee941a8436cbfdd6c')
app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix='/github_login')
app.config['SQLALCHEMY_DATABASE_URI'] = DBURL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mysecretkey'
# db = SQLAlchemy(app)

from models.bookings import db, Resturant


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/booking')
def booking():
    if not github.authorized:
        return redirect(url_for('github.login'))
    username = github.get('/user')
    if username.ok:
        user_json = username.json()
        print(user_json['name'])
        resturants = db.session.query(Resturant.resturant_name).all()
        print(resturants)
    return render_template('home.html', resturants=resturants, user_name=user_json['name'])


if __name__ == '__main__':
    app.run(debug=True)
