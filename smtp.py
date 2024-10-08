import os
import smtplib
from email.message import EmailMessage

SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
SMTP_EMAIL = os.environ["SMTP_EMAIL"]


def new_book_notification(receiver_email, receiver_name, book_name):
    text = (
        f"Draga {receiver_name},\n"
        f"Suntem incantati sa anuntăm lansarea celei mai noi carti, {book_name}! Aceasta capodopera este acum disponibila si abia asteptam sa o descoperiti."
    )

    message = EmailMessage()
    message["Subject"] = "O noua carte a ajuns la biblioteca!"
    message["From"] = SMTP_EMAIL
    message["To"] = receiver_email
    message.set_content(text, subtype="plain", charset='utf-8')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(SMTP_EMAIL, SMTP_PASSWORD)
        smtp_server.sendmail(SMTP_EMAIL, receiver_email, message.as_string())