import os

DB_HOST_URL = os.environ.get('DB_HOST_URL', "sqlite:///data.db")

#   Smtp config
MAIL_PORT = os.environ.get('MAIL_PORT', 587)
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "")
SMTP_SERVER = os.environ.get('MAIL_SERVER', "smtp.gmail.com")
MAIL_USER = os.environ.get('MAIL_USERNAME', "")
