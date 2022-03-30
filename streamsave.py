'''
Written by: Stuart Anderson
Copyright: Tobu Pengin, LLC. 2022

These utilities come as is and will not be supported.  The author or entity claims no responsibility for usage and will not support.
'''

import os
#configure your path
my_path = '/home/your_path_here/'


def select():
    return input("1 for mp4, 2 for mp3, q for quit: ")

def encode(x):
    stream = input("Input Stream: ")
    #file = input("Input Filename: ")
    if x == '1':
        os.system('youtube-dl -f mp4 -o my_path+"%(title)s.%(ext)s" ' +stream+ ' &')
    if x == '2':
        os.system('youtube-dl --extract-audio --audio-format mp3 -o my_path+"%(title)s.%(ext)s" --yes-playlist ' +stream+ ' &')

    
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
