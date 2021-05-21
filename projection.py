from matplotlib.pyplot import imread, imshow
from lib.utils2 import colorize_pointcloud
import cv2
import numpy as np
#import argparse

#path = '/media/jay/Samsung_T5/SeeingThroughFogData/lidar_hdl64_last_stereo_left/2018-02-06_16-23-51_00200.npz' 
#path_image = '/media/jay/Samsung_T5/SeeingThroughFogData/cam_stereo_left_lut/2018-02-06_16-23-51_00200.png'

path = '/media/jay/Samsung_T5/SeeingThroughFogData/lidar_hdl64_last_stereo_left/2018-10-29_16-38-10_00020.npz'
path_image = '/media/jay/Samsung_T5/SeeingThroughFogData/cam_stereo_left_lut/2018-10-29_16-38-10_00020.png'

depth = np.load(path)['arr_0'] #load .npz file
print(depth)

background_img = np.full((310,800),255) ## gray_color background
background_img = background_img.astype(np.uint8) ## FLOAT 32

projection = colorize_pointcloud(depth,radius=30) ## IMAGE_1
image = cv2.imread(path_image) ##IMAGE_2

projection = cv2.resize(projection, (800,480))
image = cv2.resize(image, (800,480))

gray = cv2.cvtColor(projection, cv2.COLOR_BGR2GRAY)

projection_crop = gray[170:480, 0:800]
image_crop = image[170:480, 0:800]

cv2.copyTo(projection_crop,projection_crop,background_img)

background_img = background_img.astype(np.float32) ## FLOAT 32
projection_crop = projection_crop.astype(np.float32) ## FLOAT 32
image_crop = image_crop.astype(np.float32) ## FLOAT 32

#### CALC SPACE ####



#### CALC E N D ####

background_img = background_img.astype(np.uint8) ## INT 8
projection_crop = projection_crop.astype(np.uint8) ## INT 8
image_crop = image_crop.astype(np.uint8) ## INT 8

cv2.imshow('PC', projection_crop)
cv2.imshow('IC', image_crop)
cv2.imshow('BG', background_img)
cv2.imwrite('image.png', image_crop)
cv2.imwrite('depth.png', background_img)
cv2.waitKey(0)
