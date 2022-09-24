from pydub import AudioSegment 
from pydub.utils import make_chunks 

myaudio = AudioSegment.from_file("speech1.wav", "wav") 
chunk_length_ms = 8000 # pydub calculates in millisec 
chunks = make_chunks(myaudio,chunk_length_ms) #Make chunks of one sec
path = 'yt/'
for i, chunk in enumerate(chunks): 
    chunk_name = "{0}.wav".format(i) 
    print ("exporting", chunk_name) 
    chunk.export(path+chunk_name, format="wav") 
