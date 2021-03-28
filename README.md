# arch-install
Another installation script for Arch Linux, not written in Bash but Python (that changes everything).

Tested with release **2021.03.01**.

These script files will allow you to install Arch Linux not only automatically, but also without blocking instructions.

For this last point to be possible, the installation will perform a very basic automatic configuration: no swap, minimal number of partitions...
Parted is also used instead of fdisk because the latter only works in interactive mode. Same thing for usermod and passwd.

The script is broken down into two parts, because the chroot interrupts the script. This chroot then calls the second script.

The installation of the GUI and a desktop environment will be up to you, as these are not limited to one choice, and the purpose of this script is not to impose one on you.

First, run the following command from the computer to be installed. This syntax allows you to import the script files located on your remote machine at the same time:

`scp [user]@[your_ip]:/[path]/[to]/[the]/[scripts]/\{arch-install_1.py,arch-install_2.py\} ./`

Then simply run the first newly downloaded script. The second script will be called by the first one:

`python arch-install_1.py`
