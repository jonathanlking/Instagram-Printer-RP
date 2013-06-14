Raspberry-Pi-Instagram-Printer
==============================

Create your own Instagram printer with a Raspberry Pi, Polaroid Pogo and web server.

Download the files using;

    sudo apt-get install git-core
    git clone git://github.com/jonathanlking/Raspberry-Pi-Instagram-Printer.git
    
You can then get the Pi to automatically update to the latest committed files on startup by adding

    git pull home/username/...locationOfParentDirectory.../Raspberry-Pi-Instagram-Printer

to /etc/rc.local


Setup the Raspberry Pi using;

    sudo sh Raspberry-Pi-Instagram-Printer/init.sh

To print once setup - you get given the printer address in the setup

    sh print.sh instagramLink printerAddress
    (e.g) sh print.sh http://instagram.com/p/Y-6a52hOmG/ 00:04:48:1B:87:7F

More to come soon...

    <Raspberry Pi Instagram Printer>
    Copyright (C) <2013>  <Jonathan King>

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
    
    Jon - http://opalfruits.net/blog/ 
    For providing a much better solution to bluetooth pairing with a Raspberry Pi than I had before.
