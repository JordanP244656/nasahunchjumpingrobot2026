import mpu6050
import time
 
# Create a new Mpu6050 object
mpu6050 = mpu6050.mpu6050(0x68)
 
while True:
    data = (mpu6050.get_gyro_data())
    print(int(data['x']))
    time.sleep(5)
    