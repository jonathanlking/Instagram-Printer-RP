#!/usr/bin/env python

import sys
import os
import urllib
import subprocess
import bluetooth

# Get the printer address from 'settings.txt'

directory = os.path.dirname(__file__)
settingsFilename = os.path.join(directory, 'settings.txt')
imageFilename = os.path.join(directory, 'temporaryImage.jpg')


try:
    with open(settingsFilename,'r') as settings:
        printerAddress = file.readline(settings).rstrip()
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
    with open(imageFilename,'w') as file:
        file.write(photo.read())
except IOError:
    print "Unable to write file"
    sys.exit()
else:
    print "Image saved locally"

# Bind the printer to rfcomm0

bindAddress = subprocess.check_output(['sudo', 'rfcomm', 'bind', '/dev/rfcomm0', printerAddress], stderr=subprocess.STDOUT)

# Check that the printer is available

# Scan for nearby bluetooth devices
nearbyDevices = bluetooth.discover_devices()

if printerAddress in str(nearbyDevices):
    print 'Printer is available'
else:
    print 'Printer not available'
    sys.exit()

# Check that the image is real
# - Don't need to worry about this, the printer already handles this

# Send to photo to be printed

sendPhoto = subprocess.Popen(['ussp-push', '/dev/rfcomm0', imageFilename, 'file.jpg'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = sendPhoto.stdout.read()
errors = sendPhoto.stderr.read()

if 'connection established' in output.lower() and 'error' not in errors.lower():
	#successfully printed
	print 'Successfully sent to printer'

else:
	print 'There was an error:', '\033[91m', errors
