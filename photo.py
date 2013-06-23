import sys
import os
import urllib
import subprocess
import bluetooth

TEMP_FILE_NAME = 'temporaryImage.jpg'

def readPrinterAddress():

	try:
		with open('settings.txt','r') as settings:
			printerAddress = file.readline(settings).rstrip()
			return printerAddress
    except IOError:
        print "Unable to read printer address, do you have a settings.txt file?"
    	sys.exit()
    	
def downloadPhotoFromLink(link):
	
	paramaters = urllib.urlencode({'link': link})
	photo = urllib.urlopen("http://instagram.jonathanlking.com/engine/link?%s" % paramaters)
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
		
# Get the image link

imageLink = ''

if len(sys.argv) > 1:
    imageLink = sys.argv[1]
else:
    print 'No link provided'
    sys.exit()
    


# Get the printer address from 'settings.txt'

printerAddress = readPrinterAddress()
print printerAddress


# Download the image to print from the link

photo = downloadPhotoFromLink(imageLink)

# Save the image to file

savePhotoWithName(photo, TEMP_FILE_NAME)