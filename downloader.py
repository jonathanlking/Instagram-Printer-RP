#!/usr/bin/env python

import urllib

photoLink = 'http://instagram.com/p/anrQQ9vA8p/'

paramaters = urllib.urlencode({'link': photoLink})
photo = urllib.urlopen("http://instagram.jonathanlking.com/engine/link?%s" % paramaters)
print photo.read()