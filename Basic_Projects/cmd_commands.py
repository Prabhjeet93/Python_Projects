import os
import sys

""" This code will run Windows commands in Python."""


# get current directory
print(os.getcwd())

# Change to different  directory
#os.chdir("C:/test")
print(os.getcwd())

file_name=os.path.join(os.getcwd(), '/data.csv')
print(os.path.realpath('data.csv'))

# print windows platform with version
print(sys.platform)

# list of directory names that constitute the current search path
print(sys.path) 

print(os.name)
print(os.error)
print(os.listdir())
print(os.mkdir("test11"))
print(os.rmdir("test11"))
