"""
Created by: Elliott roach
Created on: Sep 2024
This module is a Micro:bit MicroPython program
"""

from microbit import *

display.clear
pin16.write_digital(0)
sleep(1000)

while True:
    if button_a.is_pressed():
        pin16.write_digital(1)
        Image.YES

    if button_b.is_pressed():
        pin16.write_digital(0)
        Image.NO
