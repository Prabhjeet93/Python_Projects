import os
import speech_recognition as sr
import ffmpeg

'''
Install ffmpeg with git.
add ffmpeg to environment variabls to run ffmpeg commands directly

install ffmpeg-python with command - pip install ffmpeg-python
 Record by youself and then it will print whatever we will say.

'''
r = sr.Recognizer()

with sr.Microphone() as source:
    print('start recording')
    audio=r.listen(source)
    text= r.recognize_google(audio)
    print(text)