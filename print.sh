#
# Instaprint Shell Script v1.0
#

# Takes two arguments, the instagram link of the photo and the address of the printer

# Download the image from the server
wget http://print.jonathanlking.com/engine/link_jpg?link=$1 -O print.jpg

# Bind to the Pogo Printer
sudo rfcomm bind /dev/rfcomm0 $2 1

# Push the file to the printer
ussp-push /dev/rfcomm0 print.jpg file.jpg

