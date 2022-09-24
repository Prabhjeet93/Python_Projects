import os
import speech_recognition as sr
import ffmpeg


'''
Install ffmpeg with git.
add ffmpeg to environment variabls to run ffmpeg commands directly

install ffmpeg-python with command - pip install ffmpeg-python
This code will conver the mp4 file into mp3 and then mp3 to wav file. And then it will convert into.

Notes - 
if ffmpeg command is not working check in the environment whether it's path is added or not.

'''

# running below commands in command promt to convert mp4 file into mp3 and then in wav.

command2mp3 = "ffmpeg -i speech.mp4 speech.mp3"
command2wav = "ffmpeg -i speech.mp3 speech.wav"

os.system(command2mp3)
print('converted to mp3')

os.system(command2wav)
print('converted to wav')

r = sr.Recognizer()

with sr.AudioFile('speech.wav') as source:
    print('start recording')
    audio = r.record(source)
    # text= r.recognize_google(audio)
    # print(text)
    try:
        print(r.recognize_google(audio,language='en-US'))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
