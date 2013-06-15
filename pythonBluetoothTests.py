import bluetooth

nearbyDevices = bluetooth.discover_devices()

for bluetoothDeviceAddress in nearbyDevices:
    deviceName = bluetooth.lookup_name(bluetoothDeviceAddress)
    print "found target bluetooth device with address ", bluetoothDeviceAddress
    print "and device name", deviceName
    if "Polaroid" in deviceName:
        print "It is a polaroid Printer!"
        with open('bt','w') as file:
        file.write('6000\n')