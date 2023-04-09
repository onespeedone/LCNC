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
https://cdimage.debian.org/cdimage/bookworm_di_alpha2/amd64/iso-cd/
Flash the iso onto USB drive and follow the steps below to load Debian 12:

1. Boot from USB
2. Select 'Graphical Install'
3. Select 'English'
4. Select 'United States'
5. Select 'American English'
6. Set up your network connection
7. Choose a single word hostname
8. Domain can be left blank
9. DO NOT ENTER A ROOT PASSWORD - LEAVE BLANK
10. Enter the user's full name
11. Enter the account username
12. Enter the account password
13. Enter your timezone
14. Select 'Guided - use entire disk'
15. Select your hard drive
16. Select 'All files in one partition'
17. Select 'Finish partitioning and write changes to disk'
18. Select 'Yes'
...wait a few minues while loading...
19. Select 'Yes'
20. Select 'United States'
21. Select deb.debian.org
22. Leave proxy blank
...wait a few minutes while loading...
23. Select 'No'
24. Check 'Debian desktop environment', 'Cinnamon', and 'standard system utilities'
...wait several minues while loading...
25. Select 'Yes'
26. Select your hard drive
27. Remove the USB drive and press continue to reboot


After installing debian 12 (bookworm), log in, Download the 3 .deb files from the github repository to your downloads folder

Open a terminal and type:

    cd ~

Then install LinuxCNC by entering:

    sudo apt install linuxcnc-uspace linuxcnc-uspace-dev mesaflash

## Restart your computer ##


**Once you have installed linuxcnc, open linuxcnc and start the axis sime briefly and then you can shut it down.  this creates the folders where probe basic will copy the sim configs to.**


**Installing QtPyVCP and Probe Basic**

**1-  Go to the location of the downloaded .deb files, right click and select "Open in terminal" in that directory.**

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
