#libraries for getting temperature data
import time
import adafruit_mlx90640
import board
import busio
import sys
import os
import math 
import numpy as np
# import pygame
# from scipy.interpolate import griddata
# from colour import Color

#---------------------------Initializing the Setup of the IR MLX Camera---------------------------------------------------------------------
#MLX IR Camera Specifics Information and Setup
i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
mlx = adafruit_mlx90640.MLX90640(i2c) #initialize the mlx sensor
print("MLX addr detected on I2C")
print([hex(i) for i in mlx.serial_number])
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

#let the mlx sensor initialize
time.sleep(1)
temp_frame = [0]*768 #initializing the temperature frame
print(mlx.getFrame(temp_frame))

#---------------------------Code for setting up the Thermal Camera GUI with PyGame---------------------------------------------------------------
 
# #Setting up the min/max values for the test of the cameras (for body heat temperature)
# MINTEMP = 19.
# MAXTEMP = 35.
 
# #Number of color values for the GUI
# COLORDEPTH = 1024

# #Initialize the environment to point data to the output for raspberry pi
# os.putenv('SDL_FBDEV', '/dev/fb1')
# pygame.init()

# ''' Used for Bicubic Interpolation - may be necessary for final deliverable 
# # pylint: disable=invalid-slice-index
# points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 728)] #generates the largest integer and remainders
# grid_x, grid_y = np.mgrid[0:31:32j, 0:23:32j]
# # pylint: enable=invalid-slice-index
# '''

# #sensor is a 32x24 grid so make an exact grid
# height = 24
# width = 32
 
# #the list of colors from the colour librarywe can choose from to generate the heat map
# blue = Color("indigo")
# colors = list(blue.range_to(Color("red"), COLORDEPTH))
 
# #create a numerical RGB array for the colors
# colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]
 
# ########What is this code for???? 
# displayPixelWidth = width / 30
# displayPixelHeight = height / 30
# #############
# #  
# lcd = pygame.display.set_mode((width, height))
 
# lcd.fill((191, 128, 255)) #make starting color purple
 
# pygame.display.update()
# pygame.mouse.set_visible(False) #no need for the mouse
 
# lcd.fill((0, 0, 0))
# pygame.display.update()
 
# #some utility functions for creating color values from the heat data
# def constrain(val, min_val, max_val):
#     return min(max_val, max(min_val, val))
 
# def map_value(x, in_min, in_max, out_min, out_max):
#     return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 

#--------------------------- Populating the Thermal Camera GUI in Realtime with the collected IR data---------------------------------------------------------------

# while True:
#     stamp = time.monotonic()
#     try:
#         mlx.getFrame(temp_frame) #gets the temperature values as a 768 size frame dimension
#     except ValueError:  
#         # these happen, no biggie - retry
#         continue
#     temp_colors = [map_value(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for t in temp_frame] #converts the temperature values in the frame to a pixel color depth

#     '''bicubic interpolation code
#     bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
#     '''     
#     #draw the data on the GUI
#     for row in range(24): #get the row data
#         for col in range(32): #get the column data:
#             pygame.draw.rect(lcd,  #surface where the rectangle is drawn on
#                              colors[constrain(int(pixel), 0, COLORDEPTH- 1)], #color representation of the pixel value
#                              (displayPixelHeight * ix, displayPixelWidth * jx, #dimensions for the square polygon
#                               displayPixelHeight, displayPixelWidth))
 
#     pygame.display.update()

# #link to the original code: https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor/raspberry-pi-thermal-camera 