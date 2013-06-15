#!/usr/bin/python

import subprocess


cmd = subprocess.Popen('hciconfig hci0', shell=True, stdout=subprocess.PIPE)
for line in cmd.stdout:
    if "BD Address" in line:
        data = line.split()
        for field in data:
            if field.len() == 'XX:XX:XX:XX:XX:XX'.len():
                print field
            
        
