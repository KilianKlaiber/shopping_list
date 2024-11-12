import imaplib
import os

EMAILADDRESS = os.getenv("EMAILADRESS")
EMAILPASSWORD = os.getenv("EMAILPASSWORD")


with imaplib.IMAP4_SSL("imap.gmail.com", 993) as connection:
    connection.login(EMAILADDRESS,EMAILPASSWORD)