import numpy as np
import math
import matplotlib.pyplot as plt

def def_mask(mask_size):
    mask = np.random.randint(0,2,mask_size) #ランダムで0,1の配列を生成する(1:開放, )
    return mask

def  def_source_pos(ang, power):
    tnkyu = np.zeros(180)   #0~180度のゼロ配列を生成
    for (theta, flux) in zip(ang, power):
        tnkyu[theta] = flux      #定義した天体の配列に、Fluxを代入
    return tnkyu

def create_detec_image(mask_size, mask, ang, power, fl):
    detec = np.zeros(mask_size*3)   #検出器に落ちるFlux
    center = round(len(detec)/2)    #検出器の中心

    #fl = mask_size
    for (theta, flux) in zip(ang, power):
        cell = round(fl*math.tan(math.radians(theta)))  #天体の天頂角に応じて、検出器に落ちる影の位置を定義
        #print("cell num : {}".format(cell))

        for i in range(len(mask)):
            if center + cell + i < len(detec):
                detec[center + cell + i - int(len(mask)/2)] += flux * mask[i]   #マスクの影が検出器に入る位置にFluxを代入
    return detec

def decode_image(mask, detec, fl):
    decode_image = []   #相関を取った配列

    for i in range(len(detec)):
        temp = 0
        if i < len(detec) - len(mask) + 1:  #検出器の各pixelごとに計算(検出器の長さ-マスクの長さ、までで相関をとる)
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
        source.append(math.degrees(math.atan((pos[i]-center+ int(len(mask)/2))/fl)))    #相関を取った配列から、天体の位置を復元

    return source, decode_image
