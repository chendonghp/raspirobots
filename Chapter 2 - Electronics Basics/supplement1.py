import gpiozero
import time


button= gpiozero.Button(17)
led= gpiozero.LED(4)

def flash():
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)

while True:
    if button.is_pressed:
        flash()
        while button.is_pressed:
            flash()
    else:
        while not button.is_pressed:
            print('not pressed')
            time.sleep(0.1)
