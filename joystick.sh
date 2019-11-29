sudo apt-get update
sudo apt-get install build-essential python-dev python-pip git -y

sudo echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
sudo echo "dwc2" | sudo tee -a /etc/modules
sudo echo "libcomposite" | sudo tee -a /etc/modules

sudo touch /usr/bin/xac_joystick_usb
sudo chmod +x /usr/bin/xac_joystick_usb

#add append line




/usr/bin/xac_joystick_usb
sudo /usr/bin/isticktoit_usb
lsmod
rmmod usb_f_hid
insmod usb_f_hid
modprobe usb_f_hid