from email.message import EmailMessage
import ssl
import smtplib
 
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
email_receiver = 'xxxxxxx@gmail.com'


# Set the subject and body of the email
subject = 'This is my first email'
body = 'Try this new way to automate email in python. Its cool.'

em = EmailMessage()
em['From'] = email_Sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context1 = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context1) as smtp:
    smtp.login(email_Sender, sender_pass_key)
    smtp.sendmail(email_Sender, email_receiver, em.as_string())