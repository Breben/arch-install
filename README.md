# arch-install

Tested with release **2021.03.01**.

These script files will allow you to install Arch Linux not only automatically, but also without blocking instructions.

For this last point to be possible, the installation will perform a very basic automatic configuration: no swap, minimal number of partitions...
Parted is also used instead of fdisk because the latter only works in interactive mode. Same thing for usermod and passwd.

The script is broken down into two parts, because the chroot interrupts the script. This chroot then calls the second script.

The installation of the GUI and a desktop environment will be up to you, as these are not limited to one choice, and the purpose of this script is not to impose one on you.


## Run on a local system

1. You will only need the scripts *arch-install_1.py* and *arch-install_2.py*. Adapt the variables at the beginning of the *arch-install_2.py* file.

2. Run the following command from the computer to be installed. This syntax allows you to import the script files located on your remote machine at the same time:

`scp [user]@[your_ip]:/[path]/[to]/[the]/[scripts]/\{arch-install_1.py,arch-install_2.py\} ./`

3. Then simply run the first transferred script. The second script will be called by the first one:

`python arch-install_1.py`


## Deployment on local network

When launching the Arch Linux installation media, the root account has no password assigned. SSH does not tolerate any connection to an account without a password, so you must assign one.

### On the target computer

1. If you need to change the keyboard layout, follow these instructions:
https://wiki.archlinux.org/index.php/Installation_guide#Set_the_keyboard_layout

2. You can then assign a suitable password to the root account with the `passwd` command.

### On the source computer

3. Adapt the variables at the beginning of *deployment.py* and *arch-install_2.py*.

4. Then simply run the *deployment.py* script.
