import os
import smtplib
from email.message import EmailMessage

from app.core.config import SMTP_EMAIL, SMTP_PASSWORD


def send_confirmation_email(receiver_email, token):
    text = (
    "Salut,\n\nAm primit o cerere pentru asocierea acestui email cu contul tau pe platforma Fila Library. Poti confirma asocierea prin accesarea acestui link:"
    f" https://fila-library.vercel.app/confirm-email/{token}\n\n"
    "Acest link va expira in 12 ore. Dupa aceasta perioada, va trebui sa faci o noua cerere pentru confirmarea emailului."
    " Daca nu doresti sa asociezi acest email cu contul tau, poti ignora acest mesaj.\n\n"
    "(Te rugam sa nu raspunzi la acest mesaj; este generat automat.)\n\nMultumim,\nFila Library"
    )


    message = EmailMessage()
    message["Subject"] = "Cerere asociere email"
    message["From"] = SMTP_EMAIL
    message["To"] = receiver_email
    message.set_content(text, subtype="plain", charset='us-ascii')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(SMTP_EMAIL, SMTP_PASSWORD)
        smtp_server.sendmail(SMTP_EMAIL, receiver_email, message.as_string())

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


async def book_returned_available(receiver_email, receiver_name, book_name):
    text = (
        f"Draga {receiver_name},\n"
        f"Suntem incantati sa va informam ca biblioteca a primit cartea cu numele:{book_name} si avand in vedere ca ati adaugat-o in wishlist este disponibila sa o imprumutati."
        "Va asteptam la biblioteca!"
    )

    message = EmailMessage()
    message["Subject"] = "Carte din wishlist a ajuns la biblioteca"
    message["From"] = SMTP_EMAIL
    message["To"] = receiver_email
    message.set_content(text, subtype="plain", charset='utf-8')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(SMTP_EMAIL, SMTP_PASSWORD)
        smtp_server.sendmail(SMTP_EMAIL, receiver_email, message.as_string())