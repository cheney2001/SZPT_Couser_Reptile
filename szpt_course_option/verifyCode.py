import cv2
import numpy as np
import requests
import base64


class node:
    def __init__(self, x=0, y=0, num=0):
        """
        坐标类
        :param x:
        :param y:
        :param num:
        """
        self.x = x
        self.y = y
        self.num = num

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNum(self):
        return self.num

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash("{}/{}".format(self.x, self.y))

    @staticmethod
    def sortNodeList(first, second):
        if first.getNum() > second.getNum():
            return 1
        elif first.getNum() < second.getNum():
            return -1
        else:
            return 0


class VerifyCode:
    REQUEST_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"
    GET_TOKEN_URL = "https://aip.baidubce.com/oauth/2.0/token"

    @staticmethod
    def Verify_number_precision(image: bytes, API_KEY, Secret_Key):
        """
        通过百度开放平台识别图片中数字
        通过数字识别接口
        :param image:
        :param API_KEY:

        :return:
        """
        img = base64.b64encode(image)
        params = {"image": img}
        access_token = VerifyCode._getToken(API_KEY, Secret_Key)
        request_url = VerifyCode.REQUEST_URL + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        print(response.json())
        return response.json()["words_result"][0]["words"]

    @staticmethod
    def handlerImage(img) -> bytes:
        """
        将图片进行二值化，并为其降噪生成用于合适OCR的Bytes Image
        :param img: img
        :return: img bytes
        """
        img = VerifyCode._processing_image(img)
        img = VerifyCode._around_white(img, width_pre=0.15, height_pre=0.15)
        img = VerifyCode._operate_img(img, 4)
        w, h, s = img.shape
        map = [[0 for c in range(h)] for r in range(w)]
        points = []
        for _w in range(w):
            for _h in range(h):
                if all(img[_w, _h] == [0, 0, 0]) and map[_w][_h] == 0:
                    point, map = VerifyCode._searchMap(img, _w, _h, map)
                    points.append(point)
        for p in points:
            # 区域黑色像素最大值，小于该值的区域视为噪点
            if p.getNum() <= 15:
                img = VerifyCode._readerNoise(img, p)
        img_bytes = VerifyCode._cv2ImageToBytes(img)
        return img_bytes

    @staticmethod
    def _getToken(API_KEY, Secret_Key):
        url = "{}?grant_type=client_credentials&client_id={}&client_secret={}".format(VerifyCode.GET_TOKEN_URL,
                                                                                      API_KEY,
                                                                                      Secret_Key)
        response = requests.get(url)
        return response.json()["access_token"]

    @staticmethod
    def _cv2ImageToBytes(img) -> bytes:
        """
        将cv2图片转换为bytes
        :param img:
        :return:
        """
        success, encoded_image = cv2.imencode(".png", img)
        img_bytes = encoded_image.tostring()
        return img_bytes

    @staticmethod
    def _processing_image(img: bytes):
        """
        将图像二值化
        :param img:
        :return:
        """
        img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
        ret, img = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
        return img

    @staticmethod
    def _searchMap(img, row, col, map, target=[0, 0, 0]):
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
                        img[x][y] == target):
                    if node(x=x, y=y) in seen:
                        continue
                    queue.append(node(x=x, y=y, num=front.getNum() + 1))
        return (max_point, map)

    @staticmethod
    def _readerNoise(img, point: node):
        """
        渲染噪点所在领域全部黑色像素为白色
        :param img: cv2 image
        :param point: 噪点所在位置
        :return: cv2 image
        """
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

    @staticmethod
    # 计算邻域非白色个数
    def _calculate_noise_count(img_obj, w, h):
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

    @staticmethod
    def _operate_img(img, k):
        """
        k邻域降噪
        :param img:
        :param k:
        :return:
        """
        w, h, s = img.shape
        # 从高度开始遍历
        for _w in range(w):
            # 遍历宽度
            for _h in range(h):
                if _h != 0 and _w != 0 and _w < w - 1 and _h < h - 1:
                    if VerifyCode._calculate_noise_count(img, _w, _h) < k:
                        img.itemset((_w, _h, 0), 255)
                        img.itemset((_w, _h, 1), 255)
                        img.itemset((_w, _h, 2), 255)

        return img

    @staticmethod
    def _around_white(img, width_pre: float, height_pre: float):
        """
        四周置白色
        :param img:
        :param width_pre:
        :param height_pre:
        :return:
        """
        w, h, s = img.shape
        for _w in range(w):
            for _h in range(h):
                if (_w <= w * width_pre) or (_h <= h * height_pre) or (_w >= w - w * width_pre) or (
                        _h >= h - h * height_pre):
                    img.itemset((_w, _h, 0), 255)
                    img.itemset((_w, _h, 1), 255)
                    img.itemset((_w, _h, 2), 255)
        return img
