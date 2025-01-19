import smtplib
import os
from email.message import EmailMessage

EMAILADDRESS = os.getenv("EMAILADRESS")
EMAILPASSWORD = os.getenv("EMAILPASSWORD")


def main():
    my_message = create_message("kilianklaiber@gmail.com", "Lets rock")

    send_message(my_message)


def send_message(message: str) -> None:
    """Send Email-Message

    Args:
        message (str): String representing the text of the message.
    """

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(EMAILADDRESS, EMAILPASSWORD)
        connection.send_message(message)


def create_message(To: str, content: str, subject: str = "Shopping List") -> object:
    """EmailMessage

    Args:
        To (str): EMail-Address of recipient
        content (str): Content of the message
        subject (str, optional): Subject of the message. Defaults to "Shopping List".

    Returns:
        object: Object of the type EmailMessage()
    """

    message = EmailMessage()

    message["From"] = "kilianklaiber@gmail.com"
    message["To"] = To
    message["Subject"] = subject

    message.set_content(content)

    return message


if __name__ == "__main__":
    main()
