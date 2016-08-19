#!/usr/bin/python3
# Downloads the current Astronomy Picture of the Day
# Sets the image as the desktop background - Only for Cinnamon desktops
# Coded in Python 3.5 and tested on Linux Mint
# Richard Denton - 18/08/2016
# apod-desktop v1.1

from bs4 import BeautifulSoup
import requests
import subprocess
import os
import sys

APOD_URL = 'http://apod.nasa.gov/apod/astropix.html'
IMAGE_SETTING = '"centered"'

def get_url():
    """
    Returns the URL of today's Astronomy Picture of the Day
    """

    # Open the APOD website and convert to BeautifulSoup - Exit script if the site fails to load
    apod = requests.get(APOD_URL)
    apod.raise_for_status()
    soup = BeautifulSoup(apod.content, "lxml")

    # Extract the link for the image of the day
    link = soup.select('a')
    link = str(link[1].get('href'))

    # Return the image URL if found, else exit the script
    if "jpg" in link:
        return 'http://apod.nasa.gov/apod/' + link
    else:
        sys.exit()

def download_image(url):
    """
    Takes in the URL of an image and downloads it to the current directory
    """
    # Open the URL
    res = requests.get(url)
    res.raise_for_status()

    # Create a file to contain the image and write the file to it
    image = open('APOD.jpg', 'wb')
    for chunk in res.iter_content(100000):
        image.write(chunk)
    image.close()


download_image(get_url())

# Call BASH processes to set wallpaper and settings
subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', 'file://' + os.getcwd() + '/APOD.jpg'])
subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-options', IMAGE_SETTING])
