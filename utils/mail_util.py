import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText

# try connecting to server .
from app_config import MAIL_USER, SMTP_SERVER, MAIL_PORT, MAIL_PASSWORD


def sendmail(address, message):
    try:
        message = MIMEText(message, "utf-8")
        emailcontent = EmailMessage()
        emailcontent['Subject'] = 'Booking Confirmation'
        emailcontent['From'] = MAIL_USER
        emailcontent['To'] = address
        emailcontent.set_content(message.as_string())

        server = smtplib.SMTP(SMTP_SERVER, port=MAIL_PORT)
        server.starttls()
        server.login(MAIL_USER, MAIL_PASSWORD)
        server.send_message(emailcontent)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
