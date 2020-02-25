import os
import sys
import numpy as np
from cam import *

results_dir = "/home/pi/iceicebaby/ir_cam/Results/"

def save(array, rock_id, ice_ratio, seconds_elapsed):
    dir_to_save = results_dir+str(rock_id)
    if not os.path.isdir(dir_to_save):
        os.mkdir(dir_to_save)
    np.save(dir_to_save + "/" + str(ice_ratio) + "_" + str(seconds_elapsed), array)

# Test Save
# from test_array import vals
# vals = np.array(vals)
# save(vals, 1, 0, 0)

# Test import
# f = open(results_dir+"1/0_0.npy", "rb")
# print(np.load(f))

while True:
    rock_id = input("Rock Id:  ") 
    ice_ratio = input("Ice w.t. Ratio:  ") 
    seconds_elapsed = input("s elapsed:  ") 
    input("Run? ")
    save(get_temps(), rock_id, ice_ratio, seconds_elapsed)
    print('Data has been saved \n')