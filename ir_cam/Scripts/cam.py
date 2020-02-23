import time
import board
import busio
import adafruit_mlx90640
import numpy as np 

# Setup cam 
i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
mlx = adafruit_mlx90640.MLX90640(i2c)
# print("MLX addr detected on I2C")
# print([hex(i) for i in mlx.serial_number])
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
print("Camera initalized boo")
 
def get_temps():
    capture = [0] * 768
    mlx.getFrame(capture)
    capture = np.array(capture)

    return np.reshape(capture, (24, 32))
    # return np.array([capture[row*24:row*24+32] for row in range(24)])