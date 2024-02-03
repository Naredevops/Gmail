import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Gmail credentials
GMAIL_USER = input("Enter your Gmail address: ")
GMAIL_PASSWORD = input("Enter your Gmail password: ")

# Email details
sender_email = GMAIL_USER
receiver_email = input("Enter recipient's email address: ")
subject = input("Enter email subject: ")
message_body = input("Enter email message body: ")

# Create message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Add message body
msg.attach(MIMEText(message_body, 'plain'))

# Connect to SMTP server and send email
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(GMAIL_USER, GMAIL_PASSWORD)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Failed to send email:", e)
finally:
    server.quit()

    
