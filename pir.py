from gpiozero import LED
from gpiozero import MotionSensor
import os
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
filename = "motion.jpg"
white_led = LED(17)
pir = MotionSensor(4)
white_led.off()

while True:
    pir.wait_for_motion()
    camera.capture(filename)
    print("Motion Detected. User has been notified.")
    white_led.on()
    os.system('python3 motionemail.py')
    pir.wait_for_no_motion()
    white_led.off()
    print("Motion Stopped")
