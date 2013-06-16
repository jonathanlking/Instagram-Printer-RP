#!/usr/bin/env python

import sys
import os
import urllib
import subprocess

# Get the printer address from 'settings.txt'

try:
    with open('settings.txt','r') as settings:
        printerAddress = file.read(settings)
except IOError:
    print "Unable to read printer address, do you have a settings.txt file?"
    sys.exit()

# Get the image link

imageLink = ''

if len(sys.argv) > 1:
    imageLink = sys.argv[1]
else:
    print 'No link provided'
    sys.exit()

# Download the image to print from the link

paramaters = urllib.urlencode({'link': imageLink})
photo = urllib.urlopen("http://instagram.jonathanlking.com/engine/link?%s" % paramaters)

# Save the image to file

try:
    with open('temporaryImage.jpg','w') as file:
        file.write(photo.read())
except IOError:
    print "Unable to write file"
    sys.exit()
else:
    print "Image saved locally"

# Bind the printer to rfcomm0

subprocess.call(['sudo', 'rfcomm', 'bind', '/dev/rfcomm0', printerAddress])

# Send to photo to be printed

responce = subprocess.check_call('ussp-push /dev/rfcomm0 temporaryImage.jpg file.jpg', shell=True)

print responce
print responce
print responce
print responce
print responce
