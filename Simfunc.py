import numpy as np
import math
import matplotlib.pyplot as plt

def def_mask(mask_size):
    mask = np.random.randint(0,2,mask_size)
    return mask

def  def_source_pos(ang, power):
    tnkyu = np.zeros(180)
    for (theta, flux) in zip(ang, power):
        tnkyu[theta] = flux
    return tnkyu

def create_detec_image(mask_size, mask, ang, power, fl):
    detec = np.zeros(mask_size*3)
    center = round(len(detec)/2)

    #fl = mask_size
    for (theta, flux) in zip(ang, power):
        cell = round(fl*math.tan(math.radians(theta)))
        print("cell num : {}".format(cell))
        for i in range(len(mask)):
            if center + cell + i < len(detec):
                detec[center + cell + i - int(len(mask)/2)] += flux * mask[i]
    return detec

def decode_image(mask, detec, fl):
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
    
    pos = [x for x in range(len(decode_image))]
    center = round(len(detec)/2)
    source = []
    for i in range(len(pos)):
        source.append(math.degrees(math.atan((pos[i]-center+ int(len(mask)/2))/fl)))

    return source, decode_image
