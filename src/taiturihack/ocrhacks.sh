#!/bin/bash

scrot 'shot.png' -e 'mv $f ~/images/scrot/'
gocr -i ~/images/scrot/shot.png -a 99
