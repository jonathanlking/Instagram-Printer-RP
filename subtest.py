import sys
import os
import bluetooth
import subprocess

from termcolor import colored

cmd = subprocess.Popen('ussp-push /dev/rfcomm0 temporaryImage.jpg file.jpg', shell=True, stderr=subprocess.PIPE)
output = cmd.communicate()

for line in output:
	print colored(line, 'red')
	
#'sudo rfcomm bind /dev/rfcomm0 00:04:48:1B:87:7F'
#'ussp-push /dev/rfcomm0 temporaryImage.jpg file.jpg'