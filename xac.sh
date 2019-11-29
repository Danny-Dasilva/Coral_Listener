# Created by https://github.com/milador/XAC-Virtual-Joystick
#!/bin/bash

sleep 10

# Create xac_joystick gadget
cd /sys/kernel/config/usb_gadget/



mkdir -p xac_joystick
cd xac_joystick

sudo su

# Define USB specification
echo 0x1d6b > idVendor # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Joystick Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB # USB2
echo 0xEF > bDeviceClass
echo 0x02 > bDeviceSubClass
echo 0x01 > bDeviceProtocol

# Perform localization


mkdir -p strings/0x409

echo "0123456789" > strings/0x409/serialnumber
echo "Raspberry Pi" > strings/0x409/manufacturer
echo "XAC Virtual Joystick" > strings/0x409/product

# Define the functions of the device

mkdir functions/hid.usb0
echo 0 > functions/hid.usb0/protocol
echo 0 > functions/hid.usb0/subclass
echo 3 > functions/hid.usb0/report_length

# Write report descriptor ( X and Y analog joysticks plus 8 buttons )
echo "05010904A1011581257F0901A1000930093109320933750895028102C005091901290815002501750195088102C0" | xxd -r -ps > functions/hid.usb0/report_desc

# Create configuration file

mkdir configs/c.1
mkdir configs/c.1/strings/0x409

echo 0x80 > configs/c.1/bmAttributes
echo 200 > configs/c.1/MaxPower # 200 mA
echo "XAC configuration" > configs/c.1/strings/0x409/configuration

# Link the configuration file
ln -s functions/hid.usb0 configs/c.1

# Activate device 
ls /sys/class/udc > UDC

