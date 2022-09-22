import pywhatkit

"""
This code will send the whatsapp message with time stamp from web.
We can schedule whatsapp messages.
We can send message in grpoup and also with attachments.

Prerequisiet for this code is - 
sender's whatapp has to be logged in to the browser with whatsappweb.
Then only this will work.

https://web.whatsapp.com/

launch this website and open your whatsapp and click on lik devices, Scan the QR from mobile, it will login automatically.
Then we can schdule our whatsapp messages with this code.
"""

# provide sender's whatsapp phone number with country code
phone_number = '+1111111'   



# send message 'Test'  to phone number at 6:35 PM
pywhatkit.sendwhatmsg(phone_number,'Test',18,35)
#pywhatkit.sendwhatmsg(phone_number, "Test", 7, 25, 15, True, 2)


##  Below are few examples

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg(phone_number, "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("groupname", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image(phone_number, "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("groupname", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("groupname", "Hey All!")

# Play a Video on YouTube
pywhatkit.playonyt("PyWhatKit") 