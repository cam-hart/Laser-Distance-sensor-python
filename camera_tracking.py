# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:59:37 2021

@author: camer
"""
import math
import statistics
import cv2
import numpy as np
from matplotlib import pyplot as plt
import laser_distance_fitting

video=cv2.VideoCapture(1)

def img_processing(img):
    #converting to hsv, making colour mask, filtering noise,converting to binary
    hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    low_green=np.array([40,0,230])
    high_green=np.array([70,255,255])
    green_mask = cv2.inRange(hsv_img, low_green, high_green)
    kernel = np.ones((11,11),np.float32)/121
    mean_filter = cv2.filter2D(green_mask,-1,kernel)
    #gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    binary_img=cv2.threshold(mean_filter,1,255,cv2.THRESH_BINARY_INV)[1]
    #blurred = cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)
    return binary_img

def keypoints_params(image):
    #creating blob parameters,blob detector, finding keypoints
    parameters=cv2.SimpleBlobDetector_Params()
    parameters.filterByArea=True
    parameters.minArea=30
    parameters.maxArea=2000
    parameters.filterByCircularity=True
    parameters.minCircularity=0.5
    detector=cv2.SimpleBlobDetector_create(parameters)
    keypoints=detector.detect(image)
    return keypoints
 
def keypoint_max(keypoints):
    max_size=0
    max_point=0
    for point in keypoints:
        if point.size>=max_size:
            max_size=point.size
            max_point=point
    return max_point

while True:
    column_list=[]
    row_list=[]
    for i in range(10):
        ret,img=video.read()
        img_processing(img)

        binary_img=img_processing(img)
        keypoints=keypoints_params(binary_img)
        keypoint=keypoint_max(keypoints)
        
        if keypoint!=0:
            column_list.append(keypoint.pt[0])
            row_list.append(keypoint.pt[1])
            
            img_with_keypoint = cv2.drawKeypoints(img, [keypoint], np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            cv2.imshow("keypoint",img_with_keypoint)
            
    #finding the median x,y values of the max keypoints, measuring img size and drawing crosshairs
    if len(column_list)>=1:
        x_median=statistics.median(column_list)
        y_median=statistics.median(row_list)
        #print([x_median,y_median])
        height,width,channels=img.shape
        column_line=cv2.line(img,(int(x_median),height),(int(x_median),0),(0,255,0),3)
        cv2.imshow("line",column_line)
        displacement=math.sqrt((abs(x_median-35)**2)+(abs(y_median-344)**2))
        a,b,c=laser_distance_fitting.opt_abc
        distance=np.exp((displacement-c)/a)-b
        print(distance)
    key=cv2.waitKey(1)
    
    
video.release()
cv2.destroyAllWindows()