#!/usr/bin/env python3
import os
from email.message import EmailMessage
import mimetypes
import smtplib

sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ.get('USER'))
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
attachment_path = "/tmp/processed.pdf"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

message = EmailMessage()
message['From'] = sender
message['To'] = recipient
message['Subject'] = "Upload Completed - Online Fruit Store"
message.set_content(body)

with open(attachment_path, 'rb') as ap:
     message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))

mail_server = smtplib.SMTP('localhost')
mail_server.send_message(message)
mail_server.quit()