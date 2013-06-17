import sys
import os
import bluetooth
import subprocess

cmd = subprocess.Popen('ussp-push /dev/rfcomm0 temporaryImage.jpg file.jpg', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = cmd.stdout.read()
errors = cmd.stderr.read()

print '\033[92m', 'Output:', output, '\n'
print '\033[91m', 'Errors:', errors, '\n'
	
#'sudo rfcomm bind /dev/rfcomm0 00:04:48:1B:87:7F'
#'ussp-push /dev/rfcomm0 temporaryImage.jpg file.jpg'