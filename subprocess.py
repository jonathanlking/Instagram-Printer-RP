import sys
import os
import urllib
import subprocess
import bluetooth

cmd = subprocess.Popen('hciconfig hci0', shell=True, stdout=subprocess.PIPE)
print cmd.stdout