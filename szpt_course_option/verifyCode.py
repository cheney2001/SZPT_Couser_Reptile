from aip import *
from PIL import Image
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
        img_arr = np.array(image)
        rows, cols = img_arr.shape
        print("{},{}".format(rows, cols))
        """
        创建一个记录图，绘制黑像素某个区域最大像素数量
        """
        record = []
        map = [[0 for c in range(0, cols)] for r in range(0, rows)]
        for row in range(0, rows):
            for col in range(0, cols):
                if img_arr[row][col] is False:
                    pass

    @staticmethod
    def searchMap(img_arr, row, col, target=False):
        dy = [1, -1, 0, 0, -1, 1, -1, 1]
        dx = [0, 0, -1, 1, -1, 1, 1, -1]
        queue = Queue(maxsize=0)
        node(x=row, y=col)
        queue.put(node)
        while queue.empty() is False:
            pass
