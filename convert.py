from matplotlib.pyplot import imread, imshow
from lib.utils2 import colorize_pointcloud
from lib.read import load_velodyne_scan, load_calib_data
from lib.visualization import project_3d_to_2d
import cv2
import numpy as np


scan_path = '/home/jay/catkin_all/catkin_fog/src/projection/asd.bin'
#calib_root = '/media/jay/Samsung_T5/SeeingThroughFogData'
#name_camera_calib = '/media/jay/Samsung_T5/SeeingThroughFogData/calib_cam_stereo_left.json'
#tftree = '/media/jay/Samsung_T5/SeeingThroughFogData/calib_tf_tree_full.json'

scan = load_velodyne_scan(scan_path)
velodyne_to_camera, camera_to_velodyne, P, R, vtc, radar_to_camera, zero_to_camera = load_calib_data('/media/jay/Samsung_T5/SeeingThroughFogData', '/media/jay/Samsung_T5/SeeingThroughFogData/calib_cam_stereo_left.json', '/media/jay/Samsung_T5/SeeingThroughFogData/calib_tf_tree_full.json')

ps = project_3d_to_2d(scan[:,:3].transpose(), vtc)

print(ps)




"""
#path = '/media/jay/Samsung_T5/SeeingThroughFogData/lidar_hdl64_last_stereo_left/2018-02-06_16-23-51_00200.npz' 
#path_image = '/media/jay/Samsung_T5/SeeingThroughFogData/cam_stereo_left_lut/2018-02-06_16-23-51_00200.png'

path = '/media/jay/Samsung_T5/SeeingThroughFogData/lidar_hdl64_last_stereo_left/2018-10-29_16-42-03_00960.npz'
path_image = '/media/jay/Samsung_T5/SeeingThroughFogData/cam_stereo_left_lut/2018-10-29_16-42-03_00960.png'

depth = np.load(path)['arr_0'] #load .npz file

projection = colorize_pointcloud(depth,radius=30)
image = cv2.imread(path_image)

gray = cv2.cvtColor(projection, cv2.COLOR_BGR2GRAY)

projection_crop = gray
image_crop = image

psx = projection_crop.shape[1]
psy = projection_crop.shape[0]
psy_r = int(psy*0.8)


######### CALC SECTION ##########

for x in range(0, psx):
    for y in range(0, psy_r):
        
        color_g = projection_crop.item(y,x)

        if(color_g < 50 ):
            projection_crop[y,x] = 195

#################################



cv2.imshow('PC', projection_crop)
cv2.imshow('IC', image_crop)
cv2.imwrite('depth.png', projection_crop)
cv2.imwrite('image.png',image_crop)

cv2.waitKey(0)
"""
