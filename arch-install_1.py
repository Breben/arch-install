import os, shutil

# Ensure the system clock is set up on the NTP server
os.system('timedatectl set-ntp true')

# If UEFI motherboard, create an additional EFI partition
if os.path.exists('/sys/firmware/efi/efivars'):
    os.system('parted /dev/sda mklabel gpt mkpart "efi" fat32 0% 260MiB set 1 esp on mkpart "root" ext4 260MiB 100%')

    os.system('mkfs.fat -F32 /dev/sda1')
    os.system('mkfs.ext4 /dev/sda2')

    os.mkdir('/mnt/efi')
    os.system('mount -t vfat /dev/sda1 /mnt/efi')
    os.system('mount /dev/sda2 /mnt')
else:
    os.system('parted /dev/sda mklabel msdos mkpart primary ext4 0% 100% set 1 boot on')
    
    os.system('mkfs.ext4 /dev/sda1')
    
    os.system('mount /dev/sda1 /mnt')
    
# Add to the list what you want to install
os.system('pacstrap /mnt base linux linux-firmware networkmanager python openssh nano')

# Generate an fstab file to mount partitions at startup
os.system('genfstab -U /mnt >> /mnt/etc/fstab')

# This will move the second script to the newly installed system
shutil.move('/root/arch-install_2.py', '/mnt/root/arch-install_2.py')

# Change root into the new system and run the second script from there
os.system('arch-chroot /mnt python /root/arch-install_2.py')