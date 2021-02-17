#!/bin/bash

sudo service motion stop

DATE=$(date +"%Y_%m_%d_%H%M")
fswebcam -r 1280x720 --no-banner /home/pi/Development/daily-images/$DATE.jpg
convert /home/pi/Development/daily-images/$DATE.jpg -rotate 180 /home/pi/Development/daily-images/$DATE.jpg

sudo service motion start
sudo motion
