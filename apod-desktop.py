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
    # Setup a list to contain all the links from the APOD site
    links = []

    # Open the APOD website and convert to BeautifulSoup - Exit script if the site fails to load
    apod = requests.get(APOD_URL)
    if apod.status_code != 200:
        sys.exit()
    soup = BeautifulSoup(apod.content, "lxml")

    # Extract all links and place in the links list
    for link in soup.find_all('a'):
        links.append(link.get('href'))

    # Return the image URL if found, else exit the script
    if "jpg" in str(links[1]):
        return 'http://apod.nasa.gov/apod/' + str(links[1])
    else:
        sys.exit()

def download_image(url):
    """
    Takes in the URL of an image and downloads it to the current directory
    """
    # Open the URL
    res = requests.get(url)
    if res.status_code != 200:
        sys.exit()

    # Create a file to contain the image and write the file to it
    image = open('APOD.jpg', 'wb')
    for chunk in res.iter_content(100000):
        image.write(chunk)
    image.close()


download_image(get_url())

# Call BASH processes to set wallpaper and settings
subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', 'file://' + os.getcwd() + '/APOD.jpg'])
subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-options', IMAGE_SETTING])
