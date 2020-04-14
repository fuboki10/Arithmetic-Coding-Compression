#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:00:31 2020

@author: Abdelrahman Tarek
"""
import numpy as np
import cv2
import bisect

def decode(codes, block, prop):
    decoded = np.zeros((codes.size) * block)
  
    fx = np.zeros(257)
    fx[0] = 0
    for i in range(1, 257):
        fx[i] = fx[i - 1] + prop[i - 1] 
    
    for code in range(len(codes)):
        l = 0
        u = 1
        for i in range(block):  
            t = (codes[code] - l) / (u - l)
            if t > 1:
                continue
            c = bisect.bisect_left(fx, t)
            dif = u - l
            u = l + dif * fx[c]
            l = l + dif * fx[c - 1]
            decoded[code * block + i] = c

    return decoded

encoded_path = input('Please Enter encoded file path : ')
prop_path = input('Please Enter probability file path : ')
block_size = int(input('Please Enter block size : '))
n = int(input('Please Enter image Width : '))
m = int(input('Please Enter image Heigth : '))
img_path = input('Please Enter output image path : ')


encoded = np.load(encoded_path)

print(encoded)
print(encoded.size)

prop = np.load(prop_path)

# print(prop)

decoded = decode(encoded, block_size, prop)
    
print(decoded)
print(decoded.size)

out = np.resize(decoded, (m, n))

print(out)
print(out.size)

cv2.imwrite(img_path, out)