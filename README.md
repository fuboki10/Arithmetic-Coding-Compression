# Arithmetic-Coding-Compression

Name: Abdelrahman Tarek Abdou
Sec: 1
BN: 37


## How to Run The Encoder

1. `python encoder.py`

2. Enter image path Example : `/images/img.png`

3. Enter block size Example : `4`

4. Enter data type Number
  0 => float16
  1 => float32
  2 => float64
  3 => float128

5. the output encoded file `encoded.npy` will be in the same and the probability file `prop.npy` 


## How to Run The Decoder

1. `python decoder.py`

2. Enter encoded file path Example : `encoded.npy`

3. Enter probability file path Example : `prop.npy`

4. Enter block size (it should be the same as the one you encoded with) Example : `4`

5. Enter image Width Example : `400`

6. Enter image Heigth Example : `500`

7. Enter output image path Example : `/images/output.jpg`
