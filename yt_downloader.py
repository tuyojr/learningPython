# simple youtube video downloader ©Internet Made Coder on youtube (https://youtu.be/vEQ8CXFWLZU?si=mnpg0p-kJ8THXeQG)
# to run the program, input the youtube link in the command line e.g.
# python yt_downloader.py "https://youtube.link/"
# be sure to change the download path to where you want it to be.

from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)

youtube_download = yt.streams.get_highest_resolution()

youtube_download.download('./')
