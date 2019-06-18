import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText

#   Smtp config
port = 587
password = "Zoom_123"
smtp_server = "smtp.gmail.com"
sender_email = "er.vikashchy@gmail.com"


# try connecting to server .
def sendmail(address, message):
    try:
        message = MIMEText(message, "utf-8")
        emailcontent = EmailMessage()
        emailcontent['Subject'] = 'Booking Confirmation'
        emailcontent['From'] = sender_email
        emailcontent['To'] = address
        emailcontent.set_content(message.as_string())

        server = smtplib.SMTP(smtp_server, port=port)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(emailcontent)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
