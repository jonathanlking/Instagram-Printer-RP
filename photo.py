import urllib

def savePhotoWithName(photo, name):

	try:
		with open(name,'w') as file:
			file.write(photo.read())
	except IOError:
		print "Unable to write file"
		sys.exit()
	else:
		print "Image saved locally"