"""
Created by: Elliott roach
Created on: Sep 2024
This module is a Micro:bit MicroPython program
"""

from microbit import *

display.clear
pin16: 0
sleep(1000)

while True:
    if button_a.is_pressed():
        pin16: 0
        Image.YES

    if button_b.is_pressed():
        pin16: 0
        Image.NO
