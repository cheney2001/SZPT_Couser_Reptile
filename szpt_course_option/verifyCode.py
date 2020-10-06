from aip import *
from PIL import Image, ImageDraw
import io


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
        img_bytes = io.BytesIO()
        photo.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        return img_bytes  # type : bytes

    @staticmethod
    def get_pixel(image, x, y, G, N):
        # 获取像素值
        L = image.getpixel((x, y))

        # 与阈值比较
        if L > G:
            L = True
        else:
            L = False

        nearDots = 0

        if L == (image.getpixel((x - 1, y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x - 1, y)) > G):
            nearDots += 1
        if L == (image.getpixel((x - 1, y + 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x, y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x, y + 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1, y - 1)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1, y)) > G):
            nearDots += 1
        if L == (image.getpixel((x + 1, y + 1)) > G):
            nearDots += 1

        if nearDots < N:
            return image.getpixel((x, y - 1))
        else:
            return None

    # 降噪
    # Z: 降噪次数
    @staticmethod
    def clear_noise(image, G, N, Z):
        draw = ImageDraw.Draw(image)

        for i in range(0, Z):
            for x in range(1, image.size[0] - 1):
                for y in range(1, image.size[1] - 1):
                    color = VerifyCode.get_pixel(image, x, y, G, N)
                    if color is not None:
                        draw.point((x, y), color)
