import cv2
import numpy as np
from pyzbar.pyzbar import decode
global Info

Webcam = cv2.VideoCapture(0)

while True:

    success, image = Webcam.read()
    for barcode in decode(image):
        Info = barcode.data.decode('utf-8')
        with open('QRdata.txt', 'w') as Textfile:
            Textfile.write(Info)

        print(Info)
        
    cv2.imshow('SCANNER', image)
    cv2.waitKey(0)

    

