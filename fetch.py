#!/usr/bin/env python

import sys
import os
import urllib
import subprocess
import bluetooth

# Download the image url to print

response = urllib.urlopen('http://instagram.jonathanlking.com/service?requestPrintURL');
photoURL = response.read();
if not photoURL: sys.exit()
print photoURL;
subprocess.call(['python', '/home/pi/Raspberry-Pi-Instagram-Printer/print.py', photoURL])