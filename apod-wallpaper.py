#!/usr/bin/python3
#Downloads the current Astronomy Picture of the Day
#Sets the image as the desktop background - Only for Cinnamon desktops
#Coded in Pyhton 3.5 and tested on Linux Mint
#Richard Denton - 11/08/2016

import requests
import subprocess
import os


def get_url():
    """
    Returns the URL of today's Astronomy Picture of the Day
    """
    # Open the APOD website
    apod = requests.get('http://apod.nasa.gov/apod/astropix.html')

    # Convert the HTML source code into a string
    src_code = str(apod.content)

    # Locate the URL for the image from the source code. The end of the URL is just before the word IMG
    end = src_code.find('IMG') - 6
    start = end

    # Loop to locate the start of the URL. The URL is enclosed in " " so the loop stops when reaching the first "
    while src_code[start] != '"':
        start -= 1

    return 'http://apod.nasa.gov/apod/' + src_code[start + 1:end + 1]


def download_image(url):
    """
    Takes in the URL of an image and downloads it to the current directory
    """
    # Open the URL
    res = requests.get(url)

    # Create a file to contain the image and write the file to it
    image = open('APOD.jpg', 'wb')
    for chunk in res.iter_content(100000):
        image.write(chunk)
    image.close()


download_image(get_url())

# Call BASH processes to set wallpaper and settings
subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-uri', 'file://' + os.getcwd() + '/APOD.jpg'])
subprocess.run(['gsettings', 'set', 'org.cinnamon.desktop.background', 'picture-options', '"centered"'])




