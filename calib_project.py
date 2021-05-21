from matplotlib.pyplot import imread, imshow
from lib.utils2 import colorize_pointcloud
from lib.read import load_velodyne_scan, load_calib_data
from lib.visualization import project_3d_to_2d, project_points_to_2d
import cv2
import numpy as np

#scan_path = '/media/jay/Samsung_T5/SeeingThroughFogData/lidar_hdl64_last/2018-02-03_20-48-35_00400.bin'\
scan_path = '/home/jay/2011_09_26/2011_09_26_drive_0001_sync/velodyne_points/data/0000000000.bin'
calib_root = '/media/jay/Samsung_T5/SeeingThroughFogData'
name_camera_calib = 'calib_cam_stereo_left.json'
tftree = 'calib_tf_tree_full.json'
image_path = '/home/jay/catkin_all/catkin_fog/src/projection/depth.png'

scan = load_velodyne_scan(scan_path)
"""
scan = scan.reshape(-1, 5)
scan = scan[:, [0, 1, 2, 3]]
scan[:, 3] = scan[:, 3] / 255
"""
print(scan.shape)

velodyne_to_camera, camera_to_velodyne, P, R, vtc, radar_to_camera, zero_to_camera = load_calib_data(calib_root, name_camera_calib, tftree)

ps = project_3d_to_2d(scan[:,:3].transpose(), vtc)
print(velodyne_to_camera)
img = cv2.imread(image_path)
psx = img.shape[1]
psy = img.shape[0]
psy_r = int(psy*0.8)

##############################################

for x in range(0, psx):
    for y in range(0, psy_r):
        
        color_g = projection_crop.item(y,x)

        if(color_g < 50 ):
            projection_crop[y,x] = 195

##############################################

cv2.imshow("depth", img)

#projection = colorize_pointcloud(ps, 15)

#cv2.imshow('Projection', projection)
#cv2.imwrite('asd.png', ps)
cv2.waitKey(0)




