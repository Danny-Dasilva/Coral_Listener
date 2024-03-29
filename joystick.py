# File name: joystick.py
# Author: Danny Dasilva


import os
import sys
import fcntl
import termios
import time
from time import sleep
import random



def getch():
  import sys, tty, termios
  init()
  sleep_time = 0.050
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON

  try:
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
    
    if (ch == 'd'):
        button_right(sleep_time)
    elif ch == 'w':
        button_up(sleep_time)
    elif ch == 'a':
        button_left(sleep_time)
    elif ch == 's':
        button_down(sleep_time)
    elif ch == '1':
        button_1(sleep_time)
    elif ch == '2':
        button_2(sleep_time)
    elif ch == '3':
        button_3(sleep_time)
    elif ch == '4':
        button_4(sleep_time)
    elif ch == '5':
        button_5(sleep_time)
    elif ch == '6':
        button_6(sleep_time)
    elif ch == '7':
        button_7(sleep_time)
    elif ch == '8':
        button_8(sleep_time)
    elif ch == 'q':
        clean_up() 
        sys.exit()
    else:
        clean_up()
        pass
    init()
      
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode('iso-8859-1'))
	
# Initialization 
def init():
    write_report('\x00\x00\x00')

def button_1(tf):
    write_report('\x00\x00\x01')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def button_2(tf):
    write_report('\x00\x00\x02')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def button_3(tf):
    write_report('\x00\x00\x04')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def button_4(tf):
    write_report('\x00\x00\x08')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def button_5(tf):
    write_report('\x00\x00\x10')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def button_6(tf):
    write_report('\x00\x00\x20')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def button_7(tf):
    write_report('\x00\x00\x40')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def button_8(tf):
    write_report('\x00\x00\x80')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def button_right(tf):
    write_report('\x7E\x00\x00')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def button_up(tf):
    write_report('\x00\x80\x00')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def button_left(tf):
    write_report('\x80\x00\x00')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def button_down(tf):
    write_report('\x00\x7E\x00')
    time.sleep(tf)
    write_report('\x00\x00\x00')	
	
def clean_up():
    write_report('\x00\x00\x00')

def main():
  
  while True:
        print("\nKey: '" + getch() + "'\n")





if __name__ == "__main__":
    main()
