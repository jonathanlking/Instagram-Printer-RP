Raspberry-Pi-Instagram-Printer
==============================

Create your own Instagram printer with a Raspberry Pi, Polaroid Pogo and web server.

Notes
-----

This code is designed for use with a Raspberry Pi and Polaroid Pogo and may, or may not work with a Polaroid GL10 and other hardware

Installation & Setup
--------------------

Install Git + clone the repository;

    sudo apt-get install git-core
    git clone git://github.com/jonathanlking/Raspberry-Pi-Instagram-Printer.git
    
Optional: You can then get the Pi to automatically update to the latest version on startup by adding this code to "/etc/rc.local"

    git pull home/username/...locationOfParentDirectory.../Raspberry-Pi-Instagram-Printer

Install the following packages;

    sudo apt-get install bluetooth bluez bluez-utils ussp-push python-bluetooth
    
Make sure you have a bluetooth adaptor connected and the Polaroid Pogo is on    

Now run the setup.py script - You must run as sudo as it needs to create files in the root directory

    sudo python Raspberry-Pi-Instagram-Printer/setup.py
    
Printing
--------

To print once setup use the following code - You can find the printer address in "settings.txt"

    sh print.sh instagramLink printerAddress
    
For example `sh print.sh http://instagram.com/p/Y-6a52hOmG/ 00:04:48:1B:87:7F`

License
-------

    Raspberry Pi Instagram Printer
    Copyright (C) 2013 Jonathan King

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Special thanks to:
------------------

Breakfast NY - http://instaprint.me/ - The original amazing idea, which I wish got fully backed on Kickstarter    
Jon - http://opalfruits.net/blog/ - For providing a much better solution to bluetooth pairing with a Raspberry Pi than I had before.
