import sys
import os
import bluetooth
import subprocess

cmd = subprocess.Popen('sudo rfcomm bind /dev/rfcomm0 00:04:48:1B:87:7F', shell=True, stdout=subprocess.PIPE)
print cmd.stdout.read()
print cmd.stdout.read()
print cmd.stdout.read()


#'sudo rfcomm bind /dev/rfcomm0 00:04:48:1B:87:7F'
#'ussp-push /dev/rfcomm0 temporaryImage.jpg file.jpg'