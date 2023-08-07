import numpy as np
import math
import matplotlib.pyplot as plt

def def_mask(mask_size):
    mask = np.random.randint(0,2,mask_size)
    return mask

def  def_source_pos(*args):
    return args

def create_detec_image(mask_size, mask, source_pos, fl):
    detec = np.zeros(mask_size*3)
    center = round(len(detec)/2)

    #fl = mask_size
    for item in source_pos:
        cell = round(fl*math.tan(math.radians(item)))
        for i in range(len(mask)):
            if center + item + i < len(detec):
                detec[center + item + i - int(len(mask)/2)] = mask[i]
    return detec

def decode_image(mask, detec):
    decode_image = []
    for i in range(len(detec)):
        temp = 0
        if i < len(detec) - len(mask) + 1:
            for j in range(len(mask)):
                temp += detec[i+j] * mask[j]
        elif i>= len(detec) - len(mask) + 1:
            for j in range(len(detec) - i):
                temp += detec[i+j] * mask[j]
        decode_image.append(temp)
    return decode_image