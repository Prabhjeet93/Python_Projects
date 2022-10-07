"""
How to convert a python file into exe file.
    1. $pip install pyinstaller
    2. navigate to the python file location and run below commands.
        $pyinstaller --onefile <file_name>.py
    3. It will create a exe file in the dest folder with some other files.

    I have converted below Python Youtube downloader code into exe file.
     
"""




import tkinter as tk
from tkinter import ttk

from tkinter import messagebox

from pytube import YouTube, Playlist


# Method created for the download button, which will take url and location and download the audio song
def downloadVideo():
    urltxt = urlfield.get()
    locationText=locationfield.get()
    qualityofVideo=quality_cb.get()

    #link = "https://www.youtube.com/watch?v=yV-Rb-zqong"
    yt = YouTube(urltxt)
    print("Title: ", yt.title)
    print("View: ", yt.views)
    # yd = yt.streams.get_highest_resolution()
    #yd = yt.streams.get_audio_only()
    if qualityofVideo == 'Audio':
        yd = yt.streams.get_audio_only()
    else:
        yd = yt.streams.get_by_resolution(qualityofVideo)

    # ADD FOLDER HERE
    yd.download(locationText)
    messagebox.showinfo("message","Downloading the Requested video")

# Method created for the download button, which will take url and location and download the audio song
def downloadVideoplaylist():
    urltxt = urlfield.get()
    locationText=locationfield.get()
    qualityofVideo=quality_cb.get()

    ytp = Playlist(urltxt)
    for video in ytp.videos:
        print("Title: ", ytp.title)
        ytp = video.streams.get_audio_only()
        if qualityofVideo == 'Audio':
           ytp = video.streams.get_audio_only()
        else:
           ytp = video.streams.get_by_resolution(qualityofVideo)
        # ADD FOLDER HERE
        ytp.download(locationText)
    messagebox.showinfo("message", "Downloading the Requested video")



window = tk.Tk()
window.geometry("800x600")    ## size of the window defined
window.title('YouTube Downloader')  ## Title of the window defined
window_title = tk.Label(text = "Welcome to the Youtube Downloader",    ## main heading of the page defined
                        foreground="blue",   ## color of the text defined
                        background="Red",   ## background color of the label box is defined
                        width = 80,    ### width of the label box is defined
                        height=2)    ### Height of the label box is defined

window_title.grid(row=1, column=2)

# Enter URL values
url = tk.Label(window, text="Enter YouTube URL", bg="red")   # Create a Day label
url.grid(row=3, column=0)          #set the Position of the Enter url text on the main screen
urlfield = tk.StringVar()           # Define Day field variable as String
urlfield = tk.Entry(window)             # Create a text entry box for the url
urlfield.grid(row=3, column=1)          #set the Position of the Enter urlfield box on the main screen

#Location for the download values
location = tk.Label(window, text="Enter Location for download", bg="red")   # Create a Day label
location.grid(row=5, column=0)          #set the Position of the Enter location text on the main screen
locationfield = tk.StringVar()           # Define location field variable as String
locationfield = tk.Entry(window)             # Create a text entry box for the location
locationfield.grid(row=5, column=1)          #set the Position of the Enter locationfield box on the main screen

# Dropdown for the quality of the utube video
selectquality = tk.Label(window, text="Select Video's Quality", bg="red")   # Create a Day label
selectquality.grid(row=7, column=0)
selected_quality = tk.StringVar()      ## StringVar() constructor assigned to a variable
quality_cb = ttk.Combobox(textvariable=selected_quality)   ## creating a combo box and assigning to a variable
# place the widget
quality_cb.grid(row=7, column=1)     ## position of the heading text is defined on application UI

## Array defined with some values
quality_cb['values'] = ['1080p',
         '720p',
         '480p',
         '360p',
         '144p',
         'Audio']

# prevent typing a value in the combo box
quality_cb['state'] = 'readonly'


btn_download = tk.Button(window, text="Download", fg="Red", bg="Black", command=downloadVideo)
btn_download_playlist = tk.Button(window, text="Download Playlist", fg="Red", bg="Black", command=downloadVideoplaylist)
btn_download.grid(row=4, column=2)
btn_download_playlist.grid(row=5, column=2)
window.mainloop()       # Start the GUI with above mention methods and labels