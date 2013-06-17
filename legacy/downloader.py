#!/usr/bin/env python

import urllib

photoLink = 'http://instagram.com/p/anrQQ9vA8p/'

paramaters = urllib.urlencode({'link': photoLink})
photo = urllib.urlopen("http://instagram.jonathanlking.com/engine/link?%s" % paramaters)

try:
    with open('temporaryImage.jpg','w') as file:
        file.write(photo.read())
except IOError:
    print "Unable to write file"
else:
    print "Image saved"