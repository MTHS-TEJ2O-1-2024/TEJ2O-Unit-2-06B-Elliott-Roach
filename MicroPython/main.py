"""
Created by: Elliott roach
Created on: Sep 2024
This module is a Micro:bit MicroPython program
"""

from microbit import *

display.clear
input.pin16(0)
sleep(1000)

while True:
    if button_a.is_pressed():
        input.pin16(1)
        Image.YES

    if button_b.is_pressed():
        input.pin16(0)
        Image.NO
