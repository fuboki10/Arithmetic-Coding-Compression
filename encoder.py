#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:26:58 2020

@author: Abdelrahman Tarek
"""

import numpy as np
import cv2

def encode(codes, block, prop):
    encoded = np.zeros(codes.size // block, dtype=np.float64)
    fx = np.zeros(257, dtype=np.float64)
    fx[0] = 0
    for i in range(1, 257):
        fx[i] = fx[i - 1] + prop[i - 1] 
    
    for start in range(len(encoded)):
        l = 0
        u = 1
        
        for i in range(block):
            dif = u - l
            u = l + dif * fx[int(codes[i + start * block]) + 1]
            l = l + dif * fx[int(codes[i + start * block])] 
           
        encoded[start] = (u + l) / 2
        
    return encoded
    


# read image in grayscale
img_path = './original.jpg'
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# flatten image
arr = np.array(img)
print(arr)
arr = arr.flatten()

print(arr)

# prop_list
prop_list = np.zeros(256, dtype=np.float64)

for i in range(256):
    count = (arr == i).sum()
    prop_list[i] = count / arr.size

# save prop_list
np.save('prop', prop_list)

# encode
block_size = 4

print(arr.size)
if arr.size % block_size != 0:
    arr = np.append(arr, np.zeros(arr.size % block_size)) # append array of zeros 

print(arr.size)
encoded = encode(arr, block_size, prop_list)

print(encoded)
print(encoded.size)

# save encoded
np.save('encoded', encoded)
    



