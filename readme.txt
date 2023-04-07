Linuxcnc Stuff

## Start here ###
Download the debian 12 iso from here
https://cdimage.debian.org/cdimage/bookworm_di_alpha2/amd64/iso-dvd/

After installing debian 12 (bookworm) open a terminal and type:  

cd /etc/apt/

sudo gedit sources.list

comment out (#) the 2 top lines in the file

https://drive.google.com/drive/folders/14tM4MHqLw26ebGVavKvTBb3ptx_IIcj5

**To install Probe Basic from the following .deb packages, you must install all 3 seperately using the following method:**

**Requirements:**

    - Debian 12 Bookworm
    - Python 3.11
    - Linuxcnc 2.9 or higher

**If you have not already installed linuxcnc from apt, use the following line in main terminal:**

   
    sudo apt install linuxcnc-uspace linuxcnc-uspace-dev mesaflash

## Restart your computer


**Once you have installed linuxcnc, open linuxcnc and start the axis sime briefly and then you can shut it down.  this creates the folders where probe basic will copy the sim configs to.**


**Installing QtPyVCP and Probe Basic**

**1-  Download the files into your chosen directory typically home/your-pc-name/downloads**

**2-  Go to the downloaded files location, right click and select "Open Terminal Here" in that directory.**

**3-  Inthe terminal enter the following commands one at a time and press enter, it will require your sudo password:**

    
    sudo apt install debhelper-compat dh-python python3-setuptools python3-yaml python3-pyqt5.qtmultimedia python3-pyqt5.qtquick qml-module-qtquick-controls libqt5multimedia5-plugins python3-dev python3-docopt python3-qtpy python3-pyudev python3-psutil python3-markupsafe python3-vtk9 python3-pyqtgraph python3-simpleeval python3-jinja2 python3-deepdiff python3-sqlalchemy qttools5-dev-tools python3-serial

    
    sudo dpkg -i python3-hiyapyco_0.5.1-1_all.deb


**then enter:**

    
    sudo dpkg -i python3-qtpyvcp_0.4-2_all.deb


*then enter:*

    
    sudo dpkg -i python3-probe-basic_0.5.3_all.deb


**You are all installed!  you should now be able to launch your probe basic sim or machine config from within the linuxcnc applications dropdown menu.**


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
