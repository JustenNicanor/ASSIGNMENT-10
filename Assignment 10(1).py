import cv2
#import numpy as np
from pyzbar.pyzbar import decode

image = cv2.imread('QRcode.png')
for barcode in decode(image):
    Info = barcode.data.decode('utf-8')
    print(Info)



