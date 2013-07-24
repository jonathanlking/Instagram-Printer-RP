#!/usr/bin/env python

import sys
import os
import urllib
import subprocess
import bluetooth

TEMP_FILE_NAME = 'temporaryImage.jpg'

def downloadPhotoFromLink(link):
	
	paramaters = urllib.urlencode({'link': link})
	photo = urllib.urlopen("http://instagram.jonathanlking.com/link?%s" % paramaters)
	return photo

def savePhotoWithName(photo, name):
	
	try:
		with open(name,'w') as file:
			file.write(photo.read())
	except IOError:
		print "Unable to write file"
		sys.exit()
	else:
		print "Image saved locally"

def readPrinterAddress():
	
	try:
		with open('settings.txt','r') as settings:
			printerAddress = file.readline(settings).rstrip()
			return printerAddress
	except IOError:
		print "Unable to read printer address, do you have a settings.txt file?"
		sys.exit()
	

def printerAvailable(printerAddress):
	
	# Scan for nearby bluetooth devices
	nearbyDevices = bluetooth.discover_devices()
	
	if printerAddress in str(nearbyDevices):
		return True
	else:
		return False

def sendPhotoToPrintWithFilename(filename):
	
	sendPhoto = subprocess.Popen('ussp-push /dev/rfcomm0 temporaryImage.jpg file.jpg', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output = sendPhoto.stdout.read()
	errors = sendPhoto.stderr.read()
	
	if 'connection established' in output.lower() and 'error' not in errors.lower():
		return True
	else:
		print 'There was an error:', '\033[91m', errors
		return False

# Get the printer address from 'settings.txt'

printerAddress = readPrinterAddress()

# Get the image link

imageLink = ''

if len(sys.argv) > 1:
	imageLink = sys.argv[1]
else:
	print 'No link provided'
	sys.exit()

# Download the image to print from the link

photo = downloadPhotoFromLink(imageLink)

# Save the image to file

savePhotoWithName(photo, TEMP_FILE_NAME)

# Bind the printer to rfcomm0

subprocess.check_output(['sudo', 'rfcomm', 'bind', '/dev/rfcomm0', printerAddress], stderr=subprocess.STDOUT)

# Check that the printer is available

if not printerAvailable(printerAddress):
	print "No printer"
	sys.exit()

# Check that the image is real
# - Don't need to worry about this, the printer already handles this

# Send to photo to be printed

if sendPhotoToPrintWithFilename(TEMP_FILE_NAME):
	print "Sent to printer"
