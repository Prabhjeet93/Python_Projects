""""
youtube_transcript_api: This module is used for getting the captions/subtitles from a YouTube Video. It can be installed using:

pip install youtube-transcript-api # for windows
or 
pip3 install youtube-transcript-api # for Linux and MacOs 

"""


from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
  
# assigning srt variable with the list
# of dictonaries obtained by the get_transcript() function
# mention the ID only -> https://www.youtube.com/watch?v=nxcdjsfs
#link = 'https://www.youtube.com/watch?v=MQcCr3QW1vE'
srt = YouTubeTranscriptApi.get_transcript("UEyQW-EcnY8")
  
# prints the result
# print(srt)
# print(type(srt))
# yt = YouTube(link)
# print("Title: ", yt.title)

strg = ''
for i in range(len(srt)):
    #print(ls[i]['text'])
    strg = strg+" "+srt[i]['text']

#print(strg)

#open text file
# f_name=yt.title+'.txt'
# text_file = open(f_name, "w")
text_file = open('data27.txt', "w")
 
#write string to file
text_file.write(str(strg))
 
#close file
text_file.close()