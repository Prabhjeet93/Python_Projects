#enter email id
'''
This code will find out whether the entered email id is valid or not.
Prerequisite is - we need to provid ethe mail server list - like gmail, outlook, yahoo etc.
On basis of provided server list it will comapre the input email ids.
also it will verify if email id id is proper or not.
'''

def validate_email(emailid):
    if emailid.count('@')==1 and emailid.count('.')==1:
        if emailid.count('.com')==1 and emailid.endswith('.com') :
            x1 = emailid.split("@")
            x2 = x1[1].split(".")
            if x2[0] in lst_emailid:
                print(emailid," is valid and belongs to ",x2[0]," server")
            else:
                print(emailid," Email id is wrong")
        else:
            print(emailid," Email id is wrong")
    else:
        print(emailid, " Email id is wrong")

# starting the main function
#emailid=input("enter email id: ")
email_lists = ['test@.com','test@t.com','test@tom.com','test@gmail.com','test.@gmail.com','test@outlook.com','_test@yahoo.com','.test@gmail.com','test@_cvs.com','test@gmail.com.com','test@gmail.com@gmail.com']
lst_emailid=['gmail','outlook','yahoo','college','csv']
for emailid in email_lists:
    validate_email(emailid)

