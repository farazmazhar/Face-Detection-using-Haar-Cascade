# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 19:28:13 2018

@author: faraz
"""

import cv2
import sys
import numpy as np

face_cascade = cv2.CascadeClassifier('Haar-Cascade Classifiers\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Haar-Cascade Classifiers\haarcascade_eye.xml')
glasses_cascade = cv2.CascadeClassifier('Haar-Cascade Classifiers\haarcascade_eye_tree_eyeglasses.xml')

def faceDetect(image_color, image_gray):
    # Face detection. scaleFactor = 1.3 and minNegihors = 5.
    faces = face_cascade.detectMultiScale(image_gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image_color,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = image_gray[y:y+h, x:x+w]
        roi_color = image_color[y:y+h, x:x+w]
        
        # Eyes detection. Default params.
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
        # Glasses detection. Default params.
#        eyes = eye_cascade.detectMultiScale(roi_gray)
#        for (ex,ey,ew,eh) in eyes:
#            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            
    return image_color