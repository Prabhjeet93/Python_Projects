import pywhatkit

pywhatkit.start_server()
phone_number = '4372494568'


pywhatkit.sendwhatmsg(phone_number,'Test',16,15)
#pywhatkit.sendwhatmsg(phone_number, "Test", 7, 25, 15, True, 2)