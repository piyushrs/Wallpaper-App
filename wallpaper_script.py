"""Script to fetch and set a random wallpaper from Unsplash."""
import urllib.request
import requests
import os
from dotenv import load_dotenv
import ctypes

load_dotenv()
api_key = os.getenv("ACCESS_KEY")
api_secret = os.getenv("SECRET_KEY")
directory = os.getenv("FILE_SAVE_DIRECTORY")

orientation = "landscape"
count = 1

res = requests.get(f"https://api.unsplash.com/photos/random/?orientation={orientation}&client_id={api_key}&count={count}", timeout = 10).json()


wallpaper_url = res[0]["links"]["download"]
urllib.request.urlretrieve(wallpaper_url, "wallpaper.png")

ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{directory}wallpaper.png" , 0)