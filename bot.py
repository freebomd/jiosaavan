import requests
import subprocess
import sys


title_art = r"""
      ____.__           _________                                  
    |    |__| ____    /   _____/____  _____ ___  _______    ____  
    |    |  |/  _ \   \_____  \\__  \ \__  \\  \/ /\__  \  /    \ 
/\__|    |  (  <_> )  /        \/ __ \_/ __ \\   /  / __ \|   |  \
\________|__|\____/  /_______  (____  (____  /\_/  (____  /___|  /
                             \/     \/     \/           \/     \/ """
print(title_art+'\n')


def main():

    movie_name = input("Enter Jio Saavan Url:\n")
    print(f"Searching......")
    base_url = f"https://jiosaavn-api.vercel.app/link?query={movie_name}"
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    index = 0
    print("Song Name     : "+data['song'])
    print("Album         : "+data['album'])
    print("Language      : "+data['language'])
    print("Singers       : "+data['singers'])
    print("Download Link : "+data['media_url'])
    print("     Made With ❤️  By Seshu Sai")
if __name__ == "__main__":
    main()
