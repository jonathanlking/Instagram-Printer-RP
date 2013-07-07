#!/usr/bin/env python

import sys
import os
import urllib
import subprocess
import bluetooth

# Download the image url to print

response = urllib.urlopen('http://instagram.jonathanlking.com/service?requestPrintURL');
photoURL = response.read();
print photoURL;

if not photoURL: sys.exit()

subprocess.call(['python', 'print.py', photoURL])