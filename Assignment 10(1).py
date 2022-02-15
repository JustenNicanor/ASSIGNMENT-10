import cv2
import numpy as np
from pyzbar.pyzbar import decode


Webcam = cv2.VideoCapture(0)

while True:

    success, image = Webcam.read()
    for barcode in decode(image):
        Info = barcode.data.decode('utf-8')
        print(Info)


    cv2.imshow('SCANNER', image)
    cv2.waitKey(0)



