import cv2
import numpy as np
import tensorflow as tf
import json
import os
from matplotlib import pyplot as plt

save_path = ".\\Tags"

def get_textarea_tensor(filename:str):
    with open(save_path + '\\' + filename) as f:
        data = json.load(f)
        p1 = data['p1']
        p2 = data['p2']
        p3 = data['p3']
        p4 = data['p4']

    # 生成空白图像
    img = tf.zeros([200, 450])

    # 四个标定点坐标
    pts = [p1, p2, p3, p4]  # 注意，必须按顺势正或逆时针方向排序

    # 在图像上绘制多边形
    img = cv2.polylines(img.numpy(), [np.array(pts)], True, 1, thickness=1)

    # 填充内部
    img = cv2.fillPoly(img, [np.array(pts)], 1)

    # 转换为tensor
    img = tf.convert_to_tensor(img)

    return img

list_os = os.listdir(save_path)


dataset = tf.data.Dataset.from_generator(
    lambda: (get_textarea_tensor(i) for i in list_os),
    output_types=tf.float32,
    output_shapes=[200, 450]
)

'''
i = 0
for item in dataset:
    plt.imshow(item.numpy())
    plt.show()
    i += 1
    if i == 8:
        break
'''



