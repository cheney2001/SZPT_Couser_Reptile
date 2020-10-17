from szpt_course_option.courseOption import CourseOptions
from lxml import etree
from PIL import Image
import numpy as np
import io
from szpt_course_option.verifyCode import node
from queue import Queue
import collections
import cv2
import matplotlib.pyplot as plt
from szpt_course_option.verifyCode import VerifyCode

tree = lambda: collections.defaultdict(tree)


# 计算邻域非白色个数
def calculate_noise_count(img_obj, w, h):
    """
    计算邻域非白色的个数
    Args:
        img_obj: img obj
        w: width
        h: height
    Returns:
        count (int)
    """
    count = 0
    width, height, s = img_obj.shape
    for _w_ in [w - 1, w, w + 1]:
        for _h_ in [h - 1, h, h + 1]:
            if _w_ > width - 1:
                continue
            if _h_ > height - 1:
                continue
            if _w_ == w and _h_ == h:
                continue
            if (img_obj[_w_, _h_, 0] < 233) or (img_obj[_w_, _h_, 1] < 233) or (img_obj[_w_, _h_, 2] < 233):
                count += 1
    return count


# k邻域降噪
def operate_img(img, k):
    w, h, s = img.shape
    # 从高度开始遍历
    for _w in range(w):
        # 遍历宽度
        for _h in range(h):
            if _h != 0 and _w != 0 and _w < w - 1 and _h < h - 1:
                if calculate_noise_count(img, _w, _h) < k:
                    img.itemset((_w, _h, 0), 255)
                    img.itemset((_w, _h, 1), 255)
                    img.itemset((_w, _h, 2), 255)

    return img


# 四周置白色
def around_white(img, width: int, height: int):
    w, h, s = img.shape
    for _w in range(w):
        for _h in range(h):
            if (_w <= width) or (_h <= height) or (_w >= w - width) or (_h >= h - height):
                img.itemset((_w, _h, 0), 255)
                img.itemset((_w, _h, 1), 255)
                img.itemset((_w, _h, 2), 255)
    return img


def readerNoise(img, point: node):
    """
    渲染噪点所在位置相同颜色色块
    :param img_arr: np array
    :param point: node point object
    :param value: 渲染的值
    :return: np array
    """
    # dxy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    rows, cols, s = img.shape
    queue = [point]
    seen = set()
    while len(queue) != 0:
        front = queue.pop(0)
        if front in seen:
            continue
        if all(img[front.getX()][front.getY()] == [0, 0, 0]):
            img.itemset((front.getX(), front.getY(), 0), 255)
            img.itemset((front.getX(), front.getY(), 1), 255)
            img.itemset((front.getX(), front.getY(), 2), 255)
        seen.add(front)
        for i in range(len(dxy)):
            x = front.getX() + dxy[i][0]
            y = front.getY() + dxy[i][1]
            if x >= 0 and x < rows and y >= 0 and y < cols and all(
                    img[x][y] == [0, 0, 0]):
                if node(x=x, y=y) in seen:
                    continue
                queue.append(node(x=x, y=y, num=front.getNum() + 1))
    return img


def searchMap(img_arr, row, col, map, target=[0, 0, 0]):
    """
    计数 (row,col) 坐标所在位置黑色像素所占区域面积，
    返回node 类型，其有最大值坐标与最大值
    :param img_arr: cv2
    :param row: x point
    :param col: y point
    :param target: search value type
    :param map: 已进行遍历的位置记录
    :return: node object , map
    """
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    rows, cols, s = img.shape
    max_point = node(num=0)
    queue = [node(row, col, num=1)]
    seen = set()
    while len(queue) != 0:
        front = queue.pop(0)
        map[front.getX()][front.getY()] = 1
        if front in seen:
            continue
        if front.getNum() > max_point.getNum():
            max_point = front
        seen.add(front)
        for i in range(len(dxy)):
            x = front.getX() + dxy[i][0]
            y = front.getY() + dxy[i][1]
            if x >= 0 and x < rows and y >= 0 and y < cols and all(
                    img_arr[x][y] == target):
                if node(x=x, y=y) in seen:
                    continue
                queue.append(node(x=x, y=y, num=front.getNum() + 1))
    return (max_point, map)


if __name__ == "__main__":
    # img = cv2.imread('/Users/cheney/Desktop/test1.png')
    # ret, img = cv2.threshold(img, 226, 255, cv2.THRESH_BINARY)
    # plt.imshow(img)
    # plt.show()
    #
    # img = around_white(img, width=20, height=80)
    # plt.imshow(img)
    # plt.show()
    # img = operate_img(img, 4)
    # w, h, s = img.shape
    # map = [[0 for c in range(h)] for r in range(w)]
    # rec = []
    # for _w in range(w):
    #     for _h in range(h):
    #         if all(img[_w, _h] == [0, 0, 0]) and map[_w][_h] == 0:
    #             point, map = searchMap(img, _w, _h, map)
    #             rec.append(point)
    # for p in rec:
    #     if p.getNum() <= 50:
    #         img = readerNoise(img, p)
    # plt.imshow(img)
    # plt.show()
    #
    # img_bytes = VerifyCode._cv2ImageToBytes(img)
    # result = VerifyCode.verify_number(img_bytes)
    # print(result)
    with open('/Users/cheney/Desktop/test1.png', 'rb') as f:
        img = f.read()

    img = VerifyCode.handlerImage(img)
    image = Image.open(io.BytesIO(img))
    image.show()
    # plt.imshow(image)
    # plt.show()
    # print(VerifyCode.Verify_number_precision(img))
