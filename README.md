# Wallpaper Script

This script fetches a random wallpaper from Unsplash and sets it as the desktop wallpaper. It uses the Unsplash API to fetch a random image based on the specified orientation and then sets it as the wallpaper using ctypes.

## Prerequisites
- Python 3.x
- requests library
- dotenv library

## Setup
1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install the required libraries using pip: pip install requests python-dotenv

## Usage
1. Set up an Unsplash developer account and obtain an access key and secret key.
2. Create a `.env` file in the same directory as the script and add the following: ACCESS_KEY=your_access_key SECRET_KEY=your_secret_key FILE_SAVE_DIRECTORY=directory_where_you_want_to_save
3. Run the script using Python: python wallpaper_script.py
4. Alternatively, you can schedule the task.bat file in task scheduler in windows which will automatically run the script for you.

## Note
- This script is currently designed for Windows and uses the `ctypes` library to set the wallpaper. Modify the `SystemParametersInfoW` call for other operating systems.
- The script assumes the presence of a `wallpaper.png` file in the working directory.
