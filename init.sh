echo "\nThis will guide you in setting up your Raspberry Pi Instaprint"
echo "First off we need to install bluez, as this allows us to communicate over bluetooth to the Polaroid Pogo"
read null
echo "Attempting install now: \n"
sudo apt-get install bluetooth bluez bluez-utils ussp-push python-bluetooth
echo "\n"
echo "Now a quick check to make sure bluetooth is running \n"
/etc/init.d/bluetooth status
echo "\n"
echo "Make sure that the Polaroid Pogo is turned on, as we will now search for it over bluetooth \n"
read  null
hcitool scan
echo "\n\n"
echo "You should see a device entry with 'YY:YY:YY:YY:YY:YY Polaroid ZZ ZZ ZZ'"
echo "Please enter the YY:YY:YY:YY:YY:YY part with the : included \n"
read PolaroidPogoAddress
echo "As the Pogo has a bluetooth pin of '6000' we need to add it to a settings file"
echo "First we need to find the address of the bluetooth adaptor in the Pi - 'BD Address' \n\n"
read null
hciconfig hci0 -a
echo "\n"
echo "Please enter the address with the : included \n"
read AdaptorAddress
echo "Now creating file..."
cd /var/lib/bluetooth/$AdaptorAddress
echo "PolaroidPogoAddress 6000" > pincodes
echo "File created! \n"
echo "Please make a note of you Polaroid Pogo Address: $PolaroidPogoAddress"
echo "Setup Complete!"