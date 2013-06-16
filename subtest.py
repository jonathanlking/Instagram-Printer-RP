import sys
import os
import bluetooth
import subprocess

cmd = subprocess.Popen('ussp-push /dev/rfcomm0 abc.jpg file.jpg', shell=True, stdout=subprocess.PIPE)
output = cmd.stdout.read()
print output.rstrip()

#'sudo rfcomm bind /dev/rfcomm0 00:04:48:1B:87:7F'
#'ussp-push /dev/rfcomm0 temporaryImage.jpg file.jpg'