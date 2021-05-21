import gpiozero
import time

# p48 - chapter 2
# Challenge Yourself: Combine Your Button and LED Programs: 
# A program that keeps the LED turned on until the button is pressed.


button= gpiozero.Button(17)
led= gpiozero.LED(4)

while True:
    if button.is_pressed:
        led.off()
        while button.is_pressed:
            pass
    else:
        led.on()
        while not button.is_pressed:
            print('not pressed')                                                                                                                                             16        1,1          全部
