import os
import numpy as np
import cv2
from src.crowd_count import CrowdCounter
from src import network
import sys

def read_image(img_path):
    print(img_path)
    img = cv2.imread(img_path,0)
    img = img.astype(np.float32, copy=False)
    ht = img.shape[0]
    wd = img.shape[1]
    ht_1 = (ht//4)*4
    wd_1 = (wd//4)*4
    img = cv2.resize(img,(wd_1,ht_1))
    img = img.reshape((1,1,img.shape[0],img.shape[1]))
    return img

def predict(data_path):
    path =sys.argv[0]
    path=path[0:-9]

    # """Directories"""
    # data_path = 'C:/Users/Lenovo/Desktop/timg.jpg'

    model_path = path + 'r/final_models/mcnn_shtechB_110.h5'
    print(model_path)
    net = CrowdCounter()
    """Load trained model"""
    trained_model = os.path.join(model_path)
    network.load_net(trained_model, net)
    net.cuda()
    net.eval()
    gt_data = None
    """Load image from data_path"""
    im_data = read_image(data_path)
    """Calculate density map"""
    density_map = net(im_data, gt_data)
    """convert to numpy array"""
    density_map = density_map.data.cpu().numpy()
    """estimation count from density map"""
    et_count = np.sum(density_map)
    et_count = et_count.astype(np.float32, copy=False)
    print("预测人数", et_count)
    return et_count


# path =sys.argv[0]
# path=path[0:-10]
# """Directories"""
# # data_path =  path+'/predict_images/timg.jpg'
# data_path = 'C:/Users/Lenovo/Desktop/timg.jpg'
#
# model_path =path+ '/final_models/mcnn_shtechA_490.h5'
#
# net = CrowdCounter()
#
# """Load trained model"""
# trained_model = os.path.join(model_path)
# network.load_net(trained_model, net)
# net.cuda()
# net.eval()
# gt_data = None
#
# """Load image from data_path"""
# im_data = read_image(data_path)
#
# """Calculate density map"""
# density_map = net(im_data, gt_data)
#
# """convert to numpy array"""
# density_map = density_map.data.cpu().numpy()
#
# """estimation count from density map"""
# et_count = np.sum(density_map)
# et_count = et_count.astype(np.float32, copy=False)
# print("预测人数",et_count)
#
#
