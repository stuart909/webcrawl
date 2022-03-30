import os

def select():
    return input("1 for mp4, 2 for mp3, q for quit: ")

def encode(x):
    stream = input("Input Stream: ")
    #file = input("Input Filename: ")
    if x == '1':
        os.system('youtube-dl -f mp4 -o "/media/nfs/Videos/Captures/%(title)s.%(ext)s" ' +stream+ ' &')
    if x == '2':
        os.system('youtube-dl --extract-audio --audio-format mp3 -o "/media/nfs/Music/Captures/%(title)s.%(ext)s" --yes-playlist ' +stream+ ' &')

    
def menu():
    num = select()
    if num == '1' or num == '2':
        encode(num)
    elif num == 'q':
        exit()
    else:
        menu()

while(True):
    menu()
