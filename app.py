from flask import Flask
import os
from app_config import DB_HOST_URL
from db import db
from endpoints import api
from mail import mail
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_HOST_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'my_secret_key'
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASS')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

api.init_app(app)
db.init_app(app)
mail.init_app(app)


@app.before_first_request
def create_db():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
