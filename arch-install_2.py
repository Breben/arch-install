import os

# Modify these variables to suit you
TIMEZONE = "Europe/Paris" # Choose your timezone using "timedatectl list-timezones"
LOCALE = "fr_FR" 
KB_LAYOUT = "fr-latin1" # Choose your keyboard layout using "ls /usr/share/kbd/keymaps/**/*.map.gz"
HOSTNAME = "arch-vm"
LOCALDOMAIN = "localdomain" # Default localdomain
PASSWORD = "root" # Try to pick a smarter one

# Create a symbolic link to set the time zone:
os.system('ln -sf /usr/share/zoneinfo/' + TIMEZONE + ' /etc/localtime')

# Pass the operating system time to the hardware clock
os.system('hwclock --systohc')

# Uncomment the selected locale parameter
with open('/etc/locale.gen', 'r+') as f:
    content = f.read().replace('#' + LOCALE + '.UTF-8 UTF-8', LOCALE + '.UTF-8 UTF-8')
    f.seek(0)
    f.write(content)
    f.truncate()

# Generate the new locales
os.system('locale-gen')

# Set the LANG variable
with open('/etc/locale.conf', 'w') as f:
    f.write('LANG=' + LOCALE + '.UTF-8')

# Set the keyboard layout by making it persistent
with open('/etc/vconsole.conf', 'w') as f:
    f.write('KEYMAP=' + KB_LAYOUT)

# Create the hostname
with open('/etc/hostname', 'w') as f:
    f.write(HOSTNAME)

# Match hostname and localdomain
with open('/etc/hosts', 'w') as f:
    f.write("127.0.0.1\tlocalhost\n::1\t\tlocalhost\n127.0.1.1\t" + HOSTNAME + "." + LOCALDOMAIN + "\t" + HOSTNAME)

# Set the root password (encrypted by OpenSSL in SHA512)
os.system('usermod -p $(openssl passwd -6 ' + PASSWORD + ') root')

# If UEFI motherboard, adapt GRUB accordingly
if os.path.exists('/sys/firmware/efi/efivars'):
    os.system('pacman -Sy --noconfirm grub efibootmgr')
    os.system('grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB')
else:
    os.system('pacman -Sy --noconfirm grub')
    os.system('grub-install /dev/sda')

os.system('grub-mkconfig -o /boot/grub/grub.cfg')

# Enable Internet and SSH on the freshly installed system
os.system('systemctl enable NetworkManager')
os.system('systemctl enable sshd')

# After that, you will have a working system.
os.system('exit')