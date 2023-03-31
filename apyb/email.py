import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_SMTP_SERVER = "smtp.gmail.com"
GMAIL_SMTP_PORT = 465
EMAIL_NO_REPLY = "noreply@python.org.br"


def smtp_connection(username: str, password: str):
    connection = smtplib.SMTP(GMAIL_SMTP_SERVER, GMAIL_SMTP_PORT)
    connection.starttls()
    connection.login(username, password)
    return connection


def build_message(from_email: str, to_email: str, subject: str, html_body: str):
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject

    body_text = MIMEText(html_body, "html")
    message.attach(body_text)
    return message


def send_email_as_no_reply(to_email: str, subject: str, body: str, smtp_password: str):
    message = build_message(EMAIL_NO_REPLY, to_email, subject, body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(GMAIL_SMTP_SERVER, GMAIL_SMTP_PORT, context=context) as smtp:
        smtp.login(EMAIL_NO_REPLY, smtp_password)
        smtp.sendmail(EMAIL_NO_REPLY, to_email, message.as_string())
