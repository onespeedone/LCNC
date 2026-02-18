JJM 2/17/2026

Linuxcnc Stuff

Thank you to the LinuxCNC forum user Lcvette on his post at https://forum.linuxcnc.org/qtpyvcp/48373-qtpyvcp-and-probe-basic-deb-installation-files-inside
and his google drive link https://drive.google.com/drive/folders/14tM4MHqLw26ebGVavKvTBb3ptx_IIcj5

Installing Debian 13 and Linux CNC,
**Requirements:**

    - Debian 13 Trixie
    - Linuxcnc 2.9 or higher
    - Python 3.11 (optional)

## Start here ###
Download the debian 13 iso from here
https://cdimage.debian.org/debian-cd/ ** main link to ISO files - select the amd64 iso-cd file **
Debian 13 link https://cdimage.debian.org/debian-cd/13.3.0/amd64/iso-cd/
Use the CD image. During installation you can select the GUI (cinnamon is my choice)

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
...wait a few minutes while loading...
19. Select 'Yes'
20. Select 'United States'
21. Select deb.debian.org
22. Leave proxy blank
...wait a few minutes while loading...
23. Select 'No'
24. Check 'Debian desktop environment', 'Cinnamon', and 'standard system utilities'
...wait several minutes while loading...
25. Select 'Yes'
26. Select your hard drive
27. Remove the USB drive and press continue to reboot


After installing debian, log in

Open a terminal and type:

    cd ~

Then install LinuxCNC by entering:

    sudo apt install linuxcnc-uspace mesaflash

## Restart your computer ##

Realtime Kernel

As of 2/17/2026 the default kernel is a realtime kernel (preempt) when using the amd64 cd iso

To check what kernal is running open a terminal and type:

    uname -a

If you need to add a realtime kernal, open synaptics package manager and search for preempt and check the box to install the latest version. 
Restart linux and at the grub screen select advanced options and slect the realtime kernel that was just installed.

To make the default kernel be the realtime kernel open a terminal and type:

    sudo apt install grub-customizer

to run it type:

    grub-customizer

Change the default kernel to the preempt RT kernel

