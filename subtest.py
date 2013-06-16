import sys
import os
import bluetooth
import subprocess

cmd = subprocess.Popen('sudo rfcomm bind /dev/rfcomm0 00:04:48:1B:87:7F', shell=True, stderr=subprocess.PIPE)
output = cmd.communicate()
print output

#'sudo rfcomm bind /dev/rfcomm0 00:04:48:1B:87:7F'
#'ussp-push /dev/rfcomm0 temporaryImage.jpg file.jpg'