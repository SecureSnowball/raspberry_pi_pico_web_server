from machine import Pin, I2C
import utime
from time import sleep_ms

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def distance():
    timepassed = 0
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(2)
    trigger.low()
    
    signaloff = 0
    signalon = 0

    while echo.value() == 0:
        signaloff = utime.ticks_us()

    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    timepassed = signalon - signaloff
    return timepassed

while True:
    measured_time = distance()
    distance_cm = (measured_time * 0.0343) / 2
    print(distance_cm)
    sleep_ms(500)
