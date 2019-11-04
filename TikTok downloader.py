from bs4 import BeautifulSoup
import requests
import time
import os
import wget
import sys
import re

p1 = r"^https://m.tiktok.com/v/([0-9]{19})"
p2 = r"^https://www.tiktok.com/([@a-zA-Z\_0-9]+)/video/([0-9]{19})$"


def print_menu():
    print("\n\nChoose Option :- \n\n")
    print("\n1) - Without Watermarked")
    print("\n2) - With Watermarker")
    print("\n3) - Audio Only")


def get_inputs():
    while(1):
        link = str(input("URL :- "))
        if re.match(p1, link):
            link = link[:link.find("html")-1]
            break
        else:
            print("\nInvalid URL!\nTry again!\n\n")

    print_menu()

    while(1):
        try:
            opt = int(input("\n\nEnter your option :- "))
            if(opt <= 3) and (opt >= 0):
                opt -= 1
                break
        except:
            print("\nInvalid Input!\nTry again!\n\n")

    download_video(link.strip(), opt)


def download_video(link, opt):
    print(link)
    data = {
        'url': link
    }

    response = requests.post(
        'https://tiktokdownloader.net/download_ajax/', data=data)
    soup = BeautifulSoup(response.text, 'html.parser')

    contenturl = None
    for count, row in enumerate(soup.findAll('a', attrs={'rel': 'nofollow noreferrer'})):
        if count == opt:
            contenturl = row["href"]

    name = str(link).split("/")[-1]
    save_video(contenturl, name + ".mp4")


def save_video(link, name):
    cwd = str(os.getcwd())

    if os.name != "posix":
        try:
            os.mkdir(cwd + "\\Videos")
        except:
            pass

        cwd += "\\Videos\\"

        path = cwd + name
        wget.download(link, path)

    else:
        wget.download(link, name)
        
    try:
        print(path)
    except:
        pass

get_inputs()
