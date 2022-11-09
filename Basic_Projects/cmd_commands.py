import os

# str = "python for absolute beginners"
# print (str.capitalize())

# str="TURN OFF LINK LIGHTS IN PACKET TRACER FOR THIS LAB"
# print(str.lower())

print(os.getcwd())
file_name=os.path.join(os.getcwd(), '/data.csv')
print(os.path.realpath('data.csv'))