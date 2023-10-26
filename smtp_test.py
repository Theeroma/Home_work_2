from dotenv import load_dotenv
import os, smtplib

load_dotenv('.env')

def send_email(title, message, to_email):
    sender = os.environ.get('smpt_email')
    password = os.environ.get('smpt_password')

server = smtplib.SMTP('smpt.gmail.com', 587)
server.starttls()

try:
    server.login(sender, password)
    server.sendmail(sender, to_email, message)
    return "200 OK"
except Exception as error:
    return f"Error {error}"
print(send_email('Hello', "Geeks", 'romofficial958@gmail.com'))