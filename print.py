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

# Download the image to print from the link

photoLink = 'http://instagram.com/p/anrQQ9vA8p/'

paramaters = urllib.urlencode({'link': photoLink})
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

cmd = subprocess.Popen('sudo rfcomm bind /dev/rfcomm0 ' + printerAddress, shell=True, stdout=subprocess.PIPE)
for line in cmd.stdout:
    print line
    print len(line)

# Responces:
# "Can't create device: Address already in use"
# No responce = success