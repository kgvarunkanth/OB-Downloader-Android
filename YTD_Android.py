#import
import os
import sys

#Verification of dependencies
def dependency():
    try:
        import ffmpeg
    except ModuleNotFoundError:
        os.system('pip install ffmpeg')
    try:
        import yt_dlp
    except ModuleNotFoundError():
        os.system('pip install --no-deps -U yt-dlp')
    try:
        import mutagen
    except ModuleNotFoundError():
        os.system('pip install mutagen')
    try:
        import pycryptodomex
    except ModuleNotFoundError():
        os.system('pip install pycryptodomex')

dependency()

#Automated link grabbing from Termux url Opener
link = sys.argv[1]

#Assigning output directory
opdir = "'/storage/emulated/0/YTD/%(title)s.%(ext)s' "

#Download directory Verification
def dowdir():
    path = "/storage/emulated/0/YTD/"
    exist = os.path.isdir(path)
    if exist:
        codec()
    else:
        os.mkdir(path)
        codec()

#Advance download fn for advanced users :)
def advanced():
    
    os.system("yt-dlp -F " +link)
    vid = input('Video id: ')
    aid = input('Audio id: ')
    sub = input("Subtitle y/n: ")
    fit = ' -f "'
    format = fit+str(vid)+" + "+str(aid)
    
    def nsv():
        code = "yt-dlp --embed-thumbnail -o "+opdir+format+'" --merge-output-format mp4 ' +link
        os.system(code)
    
    def sv():
        print("Note: If the video doesn't have default subtitle on URL, Subtitle won't available")
        code = "yt-dlp --embed-thumbnail -o "+opdir+" -ci "+format+'" --write-sub --sub-lang en --embed-subs --merge-output-format mp4 ' +link
        os.system(code)

    if sub=="y":
        sv()

    elif sub=="n":
        nsv()

    else:
        advanced()


#Best version for lazy fellows
def best():

    code = "yt-dlp --embed-thumbnail -o "+opdir+" --format best " +link
    os.system(code)


#Video fellows
def video():
    
    print('Enter the respective code for Required Resolution:')
    print('[code] - [Resolution]')
    print('1 - 4k')
    print('2 - 2k')
    print('3 - 1080p')
    print('4 - 720p')
    print("5 - 480p")
    print('6 - 360p')
    print('7 - 240p')
    print('8 - 144p')

    i = input('Resolution Code: ')
    
    if i== "1":
        j = '2160'
        k = '4k'
    elif i== "2":
        j = "1440"
        k = '2k'
    elif i== "3":
        j = "1080"
        k = '1080p'
    elif i== "4":
        j = "720"
        k = '720p'
    elif i== "5":
        j = "480"
        k = '480p'
    elif i== "6":
        j = "360"
        k = '360p'
    elif i== "7":
        j = "240"
        k = '240p'
    elif i== "8":
        j = "144"
        k = '144p'
    
    else:
        print('Wrong Code :(')
        return video()
    
    print('Note: The video will download in '+k+' Resolution if youtube has such resolution. If not it will download the Best of resolution available in URL. And if you want to get list of available formats and different fps and quality go to advanced')

    usr = input("Do you need to go advanced mode (y/n): ")
    
    if usr=="y":
        advanced()

    elif usr=="n":

        def nsv():
            format = '"bestvideo[height<='+j+']+bestaudio[ext=m4a]/best[height<='+j+']/best[ext=m4a]" --merge-output-format mp4 '
            code = "yt-dlp --embed-thumbnail -o "+opdir+" -f "+format +link
            os.system(code)

        def sv():
            format = '"bestvideo[height<='+j+']+bestaudio[ext=m4a]/best[height<='+j+']/best[ext=m4a]" --write-sub --sub-lang en --embed-subs --merge-output-format mp4 '
            code = "yt-dlp --embed-thumbnail -o "+opdir+" -ci -f "+format +link
            os.system(code)

        subs = input('With Subtilte (y) or without subtitle (n): ')

        if subs=="y":
            sv()
        elif subs=="n":
            nsv()
        else:
            video()

    else:
        return video()


#Audio fellows
def audio():

    print('Enter the Format of audio (mp3, aac, m4a, flac....)')
    codec = input('Enter the format: ')
    code = "yt-dlp --embed-thumbnail -o "+opdir+" -x --audio-format "+codec+" "+link
    os.system(code)


#Orchestra Master
def codec():

    T = input('v or a or m or b: ')

    if T=="v":
         video()
    elif T=="m":
        advanced()
    elif T=="a":
        audio()
    elif T=="b":
        best()
    else:
        codec()


#Theme selection for orchestra
print('***Enter (v) for Video or (a) for audio or (m) for advanced or (b) for best***')

#Here Starts the Orchestra
dowdir()