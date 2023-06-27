from machine import Pin
from time import sleep

led = Pin('LED')

while True:    
    led.toggle()
    sleep(1)
