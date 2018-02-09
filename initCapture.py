# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 03:48:18 2018

@author: faraz
"""

import cv2
import sys
import numpy as np
import haarCascade as hc
    
def initCapture(cap, mirror = False):
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
    
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Set true if the feed is mirrored.
        if mirror:
            gray = cv2.flip(gray, 1)
            frame = cv2.flip(frame, 1)
            
        frame = hc.faceDetect(frame, gray)
    
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):    
            cv2.imwrite('./screengrab.jpeg', frame)
            break
        

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
def main():
    if len(sys.argv) > 1:    
        cap = cv2.VideoCapture(sys.argv[1])
    else:
        cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Capture is not opened")
    else:
        initCapture(cap, mirror = True)
    
if __name__ == '__main__':
    main()