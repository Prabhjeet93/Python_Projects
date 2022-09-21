from email import message
from email.message import EmailMessage
import ssl
import smtplib
import mimetypes
 
'''

 initial setup is required. to generate the passkey for this Automation.
 with gmail, we need to set 2 factor authentication from the security tab and after that navigate to the url
 https://myaccount.google.com/u/1/apppasswords
 signin to to your gmail account .
 steps - 1. Select apps from dropdown - other -> rovide name as python1 or anything.
          2.  Click on generate button, it will generate a 16 digit code. copy it and paste it in the "sender_pass_key" variable

'''


# Define email sender and receiver
email_Sender = 'xxxxxx@gmail.com'
sender_pass_key = "xxxxxxxx"
email_receiver = 'xxxxxx@gmail.com'


# Set the subject and body of the email
subject = 'This is my first email'
body = 'Try this new way to automate email in python. Its cool.'

em = EmailMessage()
em['From'] = email_Sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# add document to attach
attachment_path = "C:/Users/HP/Documents/GitHub/Python_Projects/Basic_Projects/email_send/example.pdf"
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)
mime_type1, mime_subtype = mime_type.split('/', 1)
print(mime_type1)
print(mime_subtype)
# attach the document to the mail
with open(attachment_path, 'rb') as ap:
    em.add_attachment(ap.read(), maintype=mime_type1, subtype=mime_subtype,filename=attachment_path)

print(message)


# Add SSL (layer of security)
context1 = ssl.create_default_context()


# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context1) as smtp:
    smtp.login(email_Sender, sender_pass_key)
    smtp.sendmail(email_Sender, email_receiver, em.as_string())