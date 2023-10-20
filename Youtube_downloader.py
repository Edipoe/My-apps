import threading
from pytube import YouTube
import validators
import time
import colorama

my_vieodw = None
your_URL = None


def is_a_valid_URL(url_link):
    global your_URL
    while True:
        your_URL = input("Please enter your URL here: ")
        return( validators.url(your_URL))


def youtube_downloader():
    global my_vieodw
    my_vieodw = YouTube(your_URL)
    print("Videoul se descarca",end="")
    my_vieodw.streams.get_highest_resolution().download()

    return my_vieodw

my = is_a_valid_URL(your_URL)


mythreats = threading.Thread(target=youtube_downloader)
mythreats.start()

while mythreats.is_alive():
    print(colorama.Fore.GREEN + "."+ colorama.Style.RESET_ALL,end=" ",flush=True)
    time.sleep(0.5)

mythreats.join()
print("\nDescarcare completa")












