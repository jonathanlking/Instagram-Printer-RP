import sys
import os
import bluetooth
import subprocess

cmd = subprocess.Popen('ussp-push /dev/rfcomm0 temporaryImage.jpg file.jpg', shell=True, stdout=subprocess.PIPE)
print cmd.stdout.read()
