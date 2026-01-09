import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_debt_notification(receiver_email: str, subject: str, body: str):
    sender_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")

    if not sender_email or not password:
        print("Xatolik: EMAIL_USER yoki EMAIL_PASSWORD .env faylida topilmadi!")
        return False

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        server.quit()

        print(f"Email muvaffaqiyatli yuborildi: {receiver_email}")
        return True
    except Exception as e:
        print(f"Email yuborishda xatolik: {e}")
        return False