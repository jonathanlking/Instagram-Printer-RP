#!/usr/bin/env python

import sys
import os
import bluetooth

print "Searching for devices..."

nearbyDevices = bluetooth.discover_devices()

if len(nearbyDevices) == 0:
    print "No bluetooth devices detected, please turn on and run this script again"
    sys.exit()

numberOfPrinters = 0

for bluetoothDeviceAddress in nearbyDevices:
    deviceName = bluetooth.lookup_name(bluetoothDeviceAddress)
    print "Found target bluetooth device with address", bluetoothDeviceAddress, "and device name", deviceName
    if "Polaroid" in deviceName:
        numberOfPrinters += 1

if numberOfPrinters > 0:
    print "Polaroid Pogo printer detected"
else:
    print "No printer detected, please turn on and run this script again"
    sys.exit()

hostDeviceAddress = '00:10:60:D2:A0:F4'
pathToBluetoothPincodeSettings = '/var/lib/bluetooth/' + hostDeviceAddress

if not os.path.exists(pathToBluetoothPincodeSettings):
    os.makedirs(pathToBluetoothPincodeSettings)

#if os.access(pathToBluetoothPincodeSettings, os.W_OK):
#    print "Can write to area"
#else:
#    print"Cannot write to area"

settingsFilePath = pathToBluetoothPincodeSettings + '/pincodes'

try:
    with open(settingsFilePath,'w') as file:
        file.write(bluetoothDeviceAddress)
        file.write(' 6000\n')
except IOError:
    print "Unable to write file, maybe you did not run as sudo?"
else:
    print "Setup complete."