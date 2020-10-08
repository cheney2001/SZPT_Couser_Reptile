from aip import *
from PIL import Image, ImageDraw
import numpy as np
import io
from queue import Queue


class node:
    def __init__(self, x=0, y=0, num=0):
        self.x = x
        self.y = y
        self.num = num

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getNum(self):
        return self.num


class VerifyCode:
    APP_ID = "22782455"
    API_KEY = "3uCM2HafGbKma7DIQgAkIzVB"
    Secret_Key = "XkrS0153qKY3PmETZN9KmbIQAeQgf9b0"

    @staticmethod
    def verify_number(image):
        client = AipOcr(VerifyCode.APP_ID, VerifyCode.API_KEY, VerifyCode.Secret_Key)
        result = client.basicGeneral(image)
        return result["words_result"][0]['words']

    @staticmethod
    def processing_image(img: bytes):
        """
        将图像二值化
        :param img:
        :return:
        """
        stream = io.BytesIO(img)
        img = Image.open(stream)
        img = img.convert('L')
        # 阀值
        threshold = 229
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)

        photo = img.point(table, '1')
        photo.show()
        # img_bytes = io.BytesIO()
        # photo.save(img_bytes, format='PNG')
        # img_bytes = img_bytes.getvalue()
        # return img_bytes  # type : bytes
        return photo

    @staticmethod
    def clearNoise(image):
        """
        清理图像噪点
        :param image: PIL Image
        :return: PIL Image
        """
        img_arr = np.array(image)
        rows, cols = img_arr.shape
        print("{},{}".format(rows, cols))
        # record 将记录拥有黑色像素块最大值的位置
        record = []
        # map 将记录已经遍历的像素点
        map = [[0 for c in range(0, cols)] for r in range(0, rows)]
        for row in range(0, rows):
            for col in range(0, cols):
                if img_arr[row][col] is False and map[row][col] == 0:
                    max_point, map = VerifyCode.searchMap(img_arr, row, col, map=map)
                    record.append(max_point)

    @staticmethod
    def searchMap(img_arr, row, col, target=False, map=None):
        """
        计数 (row,col) 坐标所在位置黑色像素所占区域面积，
        返回node 类型，其有最大值坐标与最大值
        :param img_arr: np array
        :param row: x point
        :param col: y point
        :param target: search value type
        :param map: 已进行遍历的位置记录
        :return: node object , map
        """
        dy = [1, -1, 0, 0, -1, 1, -1, 1]
        dx = [0, 0, -1, 1, -1, 1, 1, -1]
        rows, cols = img_arr.shape
        if map is None:
            map = [[0 for c in range(0, cols)] for r in range(0, rows)]
        queue = Queue(maxsize=0)
        queue.put(node(x=row, y=col))
        max_point = node(num=0)
        while queue.empty() is False:
            cur = queue.get()
            map[cur.getX()][cur.getY()] = 1
            if cur.getNum() > max_point.getNum():
                max_point = cur
            for i in range(0, 8):
                x = cur.getX() + dx[i]
                y = cur.getY() + dy[i]
                if x >= 0 and x < rows and y >= 0 and y < cols \
                        and img_arr[x][y] is target and map[x][y] == 0:
                    queue.put(node(x=0, y=0, num=cur.getNum() + 1))
        return (max_point, map)
