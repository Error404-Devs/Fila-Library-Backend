import os
import smtplib
from email.message import EmailMessage

SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
SMTP_EMAIL = os.environ["SMTP_EMAIL"]


