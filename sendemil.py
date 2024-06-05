# Code snippet for Email Automation
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

# Set up the server connection
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Login to your email account
server.login("Abelmekonn9@gmail.com", "uzesibdeivvyjuqt")

# Compose the email with attachment
message = MIMEMultipart()
message['From'] = "Abelmekonn9@gmail.com"
message['To'] = "Abelmekonn8@gmail.com"
message['Subject'] = " Happy Birthday, My Love!"

body = "Check out this attachment!"
message.attach(MIMEText(body, 'plain'))

attachment_path = "file.txt"
attachment = open(attachment_path, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename=file.txt")

message.attach(part)

# Send the email
server.sendmail("Abelmekonn9@gmail.com", "Abelmekonn8@gmail.com", message.as_string())

# Close the server connection
server.quit()