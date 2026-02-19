import os
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email(email_content):
    sender_email = os.getenv("SENDER_EMAIL")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    if not sender_email or not app_password:
        raise ValueError("Missing email credentials in .env")

    msg = EmailMessage()
    msg.set_content(email_content)
    msg["Subject"] = "PhD Proposal Inquiry"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

    print("Email sent successfully.")
