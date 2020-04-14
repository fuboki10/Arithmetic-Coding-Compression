#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:26:58 2020

@author: Abdelrahman Tarek
"""

import numpy as np
import cv2

def encode(codes, block, prop):
    encoded = np.zeros(codes.size // block, dtype=tp)
    fx = np.zeros(257, dtype=tp)
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
    
img_path = input('Please Enter image path : ')
block_size = int(input('Please Enter block size : '))
dtype = int(input('Please enter data type \n0 =>> float16\n1 =>> float32\n2 =>> float64\n3 =>> float128\n'))
if dtype > 3 or dtype < 0:
    print('Please enter valid data type')
    exit(1)

tp = None
if dtype == 0:
    tp = np.float16
elif dtype == 1:
    tp = np.float32
elif dtype == 2:
    tp = np.float64
else:
    tp = np.float128

# read image in grayscale
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# flatten image
arr = np.array(img)
print(arr)
arr = arr.flatten()

print(arr)

# prop_list
prop_list = np.zeros(256, dtype=tp)

for i in range(256):
    count = (arr == i).sum()
    prop_list[i] = count / arr.size

# save prop_list
np.save('prop', prop_list)

# encode

print(arr.size)
if arr.size % block_size != 0:
    arr = np.append(arr, np.zeros(arr.size % block_size)) # append array of zeros 

print(arr.size)
encoded = encode(arr, block_size, prop_list)

print(encoded)
print(encoded.size)

# save encoded
np.save('encoded', encoded)
    



