

import os
import sys
import fcntl  
import termios
import time
import random

def getch():

    init()
    sleep_time = 0.050
 
    ch = input("wasd : ")

    if (ch == 'd'):
        button_right(sleep_time)
    elif ch == 'w':
        button_up(sleep_time)
    elif ch == 'a':
        button_left(sleep_time)
    elif ch == 's':
        button_down(sleep_time)
    
    else:
        clean_up()
        pass
    init()

  
    return ch

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode('iso-8859-1'))

# Initialization 
def init():
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