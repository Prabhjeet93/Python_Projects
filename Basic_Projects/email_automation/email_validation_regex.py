import re
'''
This code will find out whether the entered email id is valid or not.
this code will filter the email ID on the basis of regular expression provided.

'''
# Method to filter the email ID ont he basis of regular expression.
def validate_email(emailid):
   # x = re.search("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", emailid)
    x = re.search("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-]+)\.([a-zA-Z]{2,5})$", emailid)
    if x:
        print(emailid," is valid")
    else:
        print(emailid," Email id is wrong")

# starting the main function
email_lists = ['test@.com','test@t.com','test@tom.com','test@gmail.com','test.@gmail.com','test@outlook.com','_test@yahoo.com','.test@gmail.com','test@_cvs.com','test@gmail.com.com','test@gmail.com@gmail.com']
for emailid in email_lists:
    validate_email(emailid)

