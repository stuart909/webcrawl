'''
Written by: Stuart Anderson
Copyright: Tobu Pengin, LLC. 2022
'''

import os
import requests
import lxml.html


def search(s):
    return ['url1','url2']


def get(url):
    return requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36'})

def encode(url):
    os.system('youtube-dl -f mp4 -o "/media/nfs/Videos/Captures/%(title)s.%(ext)s" ' +url)
    

def page(url):
    resp = get(url)
    tree = lxml.html.fromstring(resp.text)
    data = []

    for i in range(2,100):
        try:
            data.append(tree.xpath('/html/body/div[1]/main/div/article/div[4]/div[1]/div[%s]/div/a' % str(i))[0].attrib['href'])
        except:
            break
    return data

lookups = [search('thing'),search('thing2')]

data = []

for i in lookups:
    for j in i:
        tmp=page(j)
        for d in tmp:
            if d not in data:
                data.append(d)

