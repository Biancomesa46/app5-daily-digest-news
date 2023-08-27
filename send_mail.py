import smtplib, ssl
import os


def send_mail(title, message):
    email = "zoikasz.nikolaszy@gmail.com"
    receiver = "zoikasz.nikolasz@gmail.com"
    password = os.getenv("PASSWORD")
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    updated_message = f"""subject: {title}
    {message}"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, email, updated_message)
