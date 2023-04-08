JJM 04/07/2023
Linuxcnc Stuff

Thank you to the LinuxCNC forum user Lcvette on his post at https://forum.linuxcnc.org/qtpyvcp/48373-qtpyvcp-and-probe-basic-deb-installation-files-inside
and his google drive link https://drive.google.com/drive/folders/14tM4MHqLw26ebGVavKvTBb3ptx_IIcj5

Installing Debian 12, Linux CNC, and Probe Basic
**Requirements:**

    - Debian 12 Bookworm
    - Python 3.11
    - Linuxcnc 2.9 or higher

## Start here ###
Download the debian 12 iso from here
https://cdimage.debian.org/cdimage/bookworm_di_alpha2/amd64/iso-dvd/

## the commenting out the sources.list file may NOT be needed if using the first ISO on this page https://cdimage.debian.org/cdimage/bookworm_di_alpha2/amd64/iso-cd/
It's annoying how many different options there are to download and not clear what the differences are.

After installing debian 12 (bookworm) open a terminal and type:  

cd /etc/apt/

sudo gedit sources.list

comment out (#) the 2 top lines in the file

	**************
	TOP 2 LINES ARE THIS:
	deb cdrom:[Debian GNU/Linux bookworm-DI-alpha2 _Bookworm_ - Official Alpha amd64 DVD Binary-1 
	with firmware 20230218-23:57]/ bookworm main non-free-firmware
	***************
Save and close the file

in your terminal type: cd ~

Download the 3 .deb files from the github repository to your downloads folder


**If you have not already installed linuxcnc from apt, use the following line in main terminal:**

   
    sudo apt install linuxcnc-uspace linuxcnc-uspace-dev mesaflash

## Restart your computer


**Once you have installed linuxcnc, open linuxcnc and start the axis sime briefly and then you can shut it down.  this creates the folders where probe basic will copy the sim configs to.**


**Installing QtPyVCP and Probe Basic**

**1-  Go to the downloaded files location, right click and select "Open in terminal" in that directory.**

**2-  Inthe terminal enter the following command and press enter, it will require your sudo password:**

    
    sudo apt install debhelper-compat dh-python python3-setuptools python3-yaml python3-pyqt5.qtmultimedia python3-pyqt5.qtquick qml-module-qtquick-controls libqt5multimedia5-plugins python3-dev python3-docopt python3-qtpy python3-pyudev python3-psutil python3-markupsafe python3-vtk9 python3-pyqtgraph python3-simpleeval python3-jinja2 python3-deepdiff python3-sqlalchemy qttools5-dev-tools python3-serial

** then enter:**

    
    sudo dpkg -i python3-hiyapyco_0.5.1-1_all.deb


**then enter:**

    
    sudo dpkg -i python3-qtpyvcp_0.4-2_all.deb


*then enter:**

    
    sudo dpkg -i python3-probe-basic_0.5.3_all.deb


**You are all installed!  you should now be able to launch your probe basic sim or machine config from within the linuxcnc applications dropdown menu.**

#########################################################################################
To get probe basic setup for your machine, follow the information here:
https://forum.linuxcnc.org/qtpyvcp/48401-py3-probe-basic-config-conversion-doc-lcnc-2-9#266123  
#########################################################################################

**To uninstall if desired, the below commands in main terminal will completely remove each package:**

    sudo dpkg -P python3-probe-basic

    sudo dpkg -P python3-hiyapyco

    sudo dpkg -P python3-qtpyvcp


#!/bin/bash

set -e

# Define a variable for the target user's home directory
TARGET_HOME="/home/${SUDO_USER:-$USER}/"

# Copy the probe_basic_sims directory to the target directory
	# Create the truetype directory if it doesn't exist
sudo -u ${SUDO_USER:-$USER} mkdir -p "${TARGET_HOME}linuxcnc/configs"
sudo -u ${SUDO_USER:-$USER} cp -r /usr/lib/python3/dist-packages/config/probe_basic/ "${TARGET_HOME}linuxcnc/configs/"
sudo -u ${SUDO_USER:-$USER} cp -r /usr/lib/python3/dist-packages/config/probe_basic_lathe/ "${TARGET_HOME}linuxcnc/configs/"
