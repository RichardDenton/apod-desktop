# apod-desktop
A simple Python script for downloading the NASA Astronomy Picture of the Day from http://apod.nasa.gov/apod/astropix.html and setting it as the desktop background.

The script has so far been tested on Linux Mint 18 with a Cinnamon desktop.

This script requires BeautifulSoup and lxml to run.

###Still to do###
* ~~Improve the method of locating the image URL - possibly using BeautifulSoup~~
* ~~Implement error checking so the script terminates if there are problems obataining the image~~
* ~~Implement easily editable options using constants~~
* Implement a check so that the whole script doesn't run if today's image has already been downloaded
* Look at the possibility of making the script work with other Linux desktops
* Look at the possibility of retaining downloaded images rather than replace the image on each run
