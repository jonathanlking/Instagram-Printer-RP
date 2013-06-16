#!/usr/bin/env python

import sys
import os
import urllib
import subprocess

photoLink = 'http://instagram.com/p/anrQQ9vA8p/'
photoLink = ''

try:
    with open('settings.txt','w') as settings:
        printerAddress = file.read(settings)
except IOError:
    print "Unable to read printer address, do you have a settings.txt file?"

paramaters = urllib.urlencode({'link': photoLink})
photo = urllib.urlopen("http://instagram.jonathanlking.com/engine/link?%s" % paramaters)
print photo.read()