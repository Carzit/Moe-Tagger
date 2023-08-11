import os
import datetime
import json

import cv2
import numpy as np

'''
tag the text area of moe-captcha
'''

# 可设置参数
dir_path = ".\\Images" # 待打标图片所在的文件夹（默认为本项目目录下的.Images/)
save_path = ".\\Tags" # 储存图片打标数据的文件夹（默认为本项目目录下的.Tags/)

with open('checkpoint.json', 'r') as f:
    checkpoint = json.load(f)
    start_index = checkpoint['stop_at_index'] # 起始图片索引（从第几张图片开始打标）
                                              # 可查看checkpoint.json中保存的最后一次打标的截至索引(stop_at_index)，将其值填入， 从该处继续打标

# 以下代码最后不要动捏
list_os = os.listdir(dir_path)
points = []

def mouse_click(event, x, y, flags, para):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(img_read, (x, y), 5, (0, 255, 0), -1)
        if len(points) > 1:
            cv2.line(img_read, points[-2], points[-1], (0, 255, 0), 2)
        if len(points) == 4:
            cv2.line(img_read, points[-1], points[0], (0, 255, 0), 2)
        cv2.imshow('img', img_read)
        print('successfully get point')

def save_checkpoint(index, name):
    last = {
        'edit_time': str(datetime.datetime.now()),
        'stop_at_index': index,
        'stop_at_image': name
    }
    with open('checkpoint.json', 'w') as f:
        json.dump(last, f)
        print('checkpoint update!')


if __name__ == '__main__':
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("img", mouse_click)

    image_index = start_index

    while True:
        img_name = dir_path + '\\' + list_os[image_index]
        json_name = save_path + '\\' + list_os[image_index].replace('.jpg', '.json')

        img_read = cv2.imread(img_name)  # the depth image
        print(f'index:{image_index}, name:{img_name}')

        cv2.imshow('img', img_read)
        if cv2.waitKey() == ord('q'): # press 'q' to quit
            save_checkpoint(image_index, img_name)
            break
        if cv2.waitKey() == ord('p'): # press 'p' to pass (next image)
            if len(points) != 4:
                save_checkpoint(image_index, img_name)
                raise ValueError(f'''标点数目有误！
                您在本张图(index:{image_index}, path:{img_name})中共标了{len(points)}个点，
                请标注文字区域四角的四个点！''')

            # 向量外积，判断凸四边形
            v1 = np.array(points[1]) - np.array(points[0])
            v2 = np.array(points[2]) - np.array(points[1])
            v3 = np.array(points[3]) - np.array(points[2])
            v4 = np.array(points[0]) - np.array(points[3])

            if ((np.cross(v1, v2) > 0 and np.cross(v2, v3) > 0 and np.cross(v3, v4) > 0 and np.cross(v4, v1) > 0)
                    or (np.cross(v1, v2) < 0 and np.cross(v2, v3) < 0 and np.cross(v3, v4) < 0 and np.cross(v4, v1) < 0)):
                dic_save = {'p1': points[0],
                            'p2': points[1],
                            'p3': points[2],
                            'p4': points[3],
                            'label': list_os[image_index][:8],
                            'index': image_index}
            else:
                save_checkpoint(image_index, img_name)
                raise RuntimeError('''标点顺序有误！
                请以顺时针或逆时针顺序标定一个凸四边形！''')

            with open(json_name, 'w') as f:
                json.dump(dic_save, f)
                print('successfully saved!')

            points.clear()
            image_index += 1
            if image_index == len(list_os):
                print('Thanks! All images have been tagged')
                break

    cv2.destroyAllWindows()