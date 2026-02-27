import time
from adafruit_servokit import ServoKit
 
kit = ServoKit(channels=16)
SERVO_CHANNEL = 0
 
kit.servo[SERVO_CHANNEL].actuation_range = 180
kit.servo[SERVO_CHANNEL].set_pulse_width_range(650, 2350)
 
current_angle = 0   
kit.servo[SERVO_CHANNEL].angle = current_angle
print("Current position set as 0")
 
time.sleep(1)
 
target_angle = current_angle + 180
target_angle = max(0, min(180, target_angle)) 
 
kit.servo[SERVO_CHANNEL].angle = target_angle
print("Moved +180°")
 
time.sleep(30)
 
kit.serVO[SERVO_CHANNEL].angle = current_angle
print("Returned to start")