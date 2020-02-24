import time
import board
import busio
import adafruit_mlx90640
import numpy as np 

# Setup cam 
i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ
print("Camera initalized boo")
 
def get_temps(exposures=3):
    all_captures = []
    for i in range(exposures):
        capture = [0] * 768 # 768 pixels
        mlx.getFrame(capture)
        all_captures.append(np.array(capture))     
    mean_array = np.mean(np.array(all_captures), axis=0)
       
    return np.reshape(mean_array, (24, 32))

