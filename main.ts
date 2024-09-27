/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: elliott
 * Created on: Sep 2024
 * This program terns on and off a light
*/

basic.clearScreen()
pins.digitalWritePin(DigitalPin.P16, 0)
basic.pause(1000)

input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Yes)
    pins.digitalWritePin(DigitalPin.P16, 1)
})

input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.No)
    pins.digitalWritePin(DigitalPin.P16, 0)
})
