import cv2
from cv2 import VideoCapture
from pyzbar.pyzbar import decode
import datetime as dt
Webcam = cv2.VideoCapture(0)

while True:

    success, camera = Webcam.read()
    for barcode in decode(camera):
        Info = barcode.data.decode('utf-8')
        timedate = dt.datetime.now()              
        Time = timedate.strftime("%H:%M")
        Date = timedate.strftime("%B %d, %Y")
        with open('QRdata.txt', 'w') as Textfile:
            Textfile.write (Info + (f"\n\n\nDate: {Date}\nTime: {Time}"))             
            Textfile.close()

        print(Info)
        print(f"\n\n\nDate: {Date}\nTime: {Time}")
    
        
        
    cv2.imshow('SCANNER',camera)
    cv2.waitKey(0)

    

