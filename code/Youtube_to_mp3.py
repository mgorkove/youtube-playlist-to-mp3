#this program downloads, in m4a format, the audio from each of the videos in a user-specified youtube playlist, 
#and saves them to the user's directory of choice.
from bs4 import BeautifulSoup
import requests
import pafy

playlist = input("Type link to the YouTube playlist to extract audio from: ") 
directory = input("Type the location of the directory to save the files to: ") 


with requests.Session() as s:
    r = s.get(playlist, allow_redirects=False)
    soup = BeautifulSoup(r.content, "lxml")
    linksList = soup.find_all("a", class_="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link ")
    prefix = "https://www.youtube.com"
    for element in linksList:
        pafyLink = pafy.new(prefix + element["href"])
        audiostreams = pafyLink.audiostreams
        for a in audiostreams:
            if a.extension == "m4a":
                a.download(filepath= directory) 
                break 
