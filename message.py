import imaplib
import os
from email.message import EmailMessage

EMAILADDRESS = os.getenv("EMAILADRESS")
EMAILPASSWORD = os.getenv("EMAILPASSWORD")


def connect() -> object:

    with imaplib.IMAP4_SSL("imap.gmail.com", 993) as connection:
        connection.login(EMAILADDRESS,EMAILPASSWORD)
        
        return connection


def create_message(To: str, content: str, subject: str="Shopping List") -> object:
    
    message = EmailMessage()

    message("From") = "kilianklaiber@gmail.com"
    message("To") = To
    message('Subject') = subject

    message.set_content(content)
    
    return message