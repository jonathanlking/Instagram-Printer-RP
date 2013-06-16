import sys
import os
import bluetooth
import subprocess

cmd = subprocess.Popen('hciconfig hci0', shell=True, stdout=subprocess.PIPE)
print cmd.stdout