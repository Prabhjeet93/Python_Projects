""""
youtube_transcript_api: This module is used for getting the captions/subtitles from a YouTube Video. It can be installed using:

pip install youtube-transcript-api # for windows
or 
pip3 install youtube-transcript-api # for Linux and MacOs 

"""


from youtube_transcript_api import YouTubeTranscriptApi
  
# assigning srt variable with the list
# of dictonaries obtained by the get_transcript() function
# mention the ID only -> https://www.youtube.com/watch?v=nxcdjsfs
srt = YouTubeTranscriptApi.get_transcript("nxcdjsfs")
  
# prints the result
# print(srt)
# print(type(srt))

strg = ''
for i in range(len(srt)):
    #print(ls[i]['text'])
    strg = strg+" "+srt[i]['text']

print(strg)

#open text file
text_file = open("data.txt", "w")
 
#write string to file
text_file.write(str(strg))
 
#close file
text_file.close()