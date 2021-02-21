from flask import Flask
from flask_mail import Mail
from .config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = 'abc876'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''

mail = Mail(app)
from app import views
