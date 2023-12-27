"""Script to fetch and set a random wallpaper from Unsplash."""
import urllib.request
import requests
import os
# from  pprint import pprint
from dotenv import load_dotenv
# from PIL import Image
import ctypes

load_dotenv()
api_key = os.getenv("ACCESS_KEY")
api_secret = os.getenv("SECRET_KEY")

orientation = "landscape"
count = 1

res = requests.get(f"https://api.unsplash.com/photos/random/?orientation={orientation}&client_id={api_key}&count={count}").json()

# pprint(res[0], indent= 4, depth= 3)

wallpaper_url = res[0]["links"]["download"]
# wallpaper_url
urllib.request.urlretrieve(wallpaper_url, "wallpaper.png")

# img = Image.open(r"wallpaper.png")
# img.show()

ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\OneDrive\Practice\Wallpaper App\wallpaper.png" , 0)