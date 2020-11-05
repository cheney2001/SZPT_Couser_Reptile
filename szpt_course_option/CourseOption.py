import collections
import requests
import os
import time
from lxml import etree
from .verifyCode import VerifyCode

tree = lambda: collections.defaultdict(tree)


class CourseOptions:
    """
    查询选修课表 , 用户登录验证码使用百度开放平台数字识别，

    :return course json
    {
        "course": {
            "week3": [
                    {
                      "course": "课程名称",
                      "day": 2(星期几),
                      "teacher": "任教老师",
                      "location": "上课地点",
                      "remark": "课程备注",
                      "node": 5(第几节)
                    },
                    ...
            ],
            "week4":[...],
            ...
        }
    }

    """
    MAP_DAYS = {
        '星期一': 1,
        '星期二': 2,
        '星期三': 3,
        '星期四': 4,
        '星期五': 5,
        '星期六': 6,
        '星期日': 7,
        '星期天': 7,
    }

    def __init__(self, API_KEY, Secret_Key, host_name, auth=None, save_verify_img_path=None):
        """
        初始化一个选修课爬虫类，需要使用百度开放平台进行验证码识别，
        可选 save_verify_img_path
        :param API_KEY: 百度开放平台API_KEY
        :param Secret_Key: 百度开放平台Secret_Key
        :param host_name: 课表域名
        :param auth: 认证方式
        :param save_verify_img_path: (可选) 正确验证码保存路径
        """
        self._login_url = "http://{}/SzptJwBsII/Secure/login.aspx".format(host_name)
        self._verify_url = "http://{}/SzptJwBsII/Secure/JpegImage.aspx".format(host_name)
        self._course_view_url = "http://{}/szptjwbsII/RandSchedule.aspx".format(host_name)
        self._ref_url = "http://{}/SzptJwBsII/default.aspx".format(host_name)

        self._form = {
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': '',
            '__VIEWSTATEGENERATOR': '210E3F16',
            '__VIEWSTATEENCRYPTED': '',
            '__EVENTVALIDATION': '',
            'ddlUserType': 0
        }
        self._headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.68"
        }
        self._cookie = {}
        self._session = requests.Session()
        self._session.auth = auth
        self._session.verify = False
        self._login_status = False
        self._verify_img = None
        self._API_KEY = API_KEY
        self._Secret_Key = Secret_Key
        self._save_path = save_verify_img_path

    def refresh_status(self):
        """
        刷新登录页面状态
        :return:
        """
        result = self._session.get(self._login_url, verify=False)
        tree = etree.HTML(result.text)
        self._form['__VIEWSTATE'] = self._match_tag_value_by_name(tree, "input", "__VIEWSTATE")
        self._verify_img = self._session.get(self._verify_url).content

    def _getVerifyCode(self):
        """
        验证码图片，并进行识别
        :return: 正确验证码
        """
        self.refresh_status()
        img = VerifyCode.handlerImage(self._verify_img)
        verify_code = VerifyCode.Verify_number_precision(img, API_KEY=self._API_KEY, Secret_Key=self._Secret_Key)
        print(verify_code)
        if len(str(verify_code)) < 5:
            print("验证码识别错误，尝试重新识别")
            time.sleep(1)
            verify_code = self._getVerifyCode()
            return verify_code
        else:
            return verify_code

    def login(self, username, password):
        """
        登陆教务系统
        :param username: 账号
        :param password: 密码
        :return:
        """
        self.refresh_status()
        data = self._form.copy()
        data["__EVENTTARGET"] = "btnLogin"
        data['txtLogin'] = username
        data['txtPwd'] = password
        data['CodeNumberTextBox'] = self._getVerifyCode()
        headers = self._getHeaders(Referer=self._login_url)
        response = self._session.post(url=self._login_url, data=data, headers=headers, allow_redirects=False)
        if response.status_code == 302:
            self._cookie.update(response.cookies.get_dict())
            headers = self._getHeaders(Referer=self._ref_url)
            response = self._session.get(self._ref_url, headers=headers)

            if response.status_code == 200:
                self._login_status = True
                print("登陆成功")
                if self._save_path is not None:
                    self._saveLoginSuccessVerifyCode(self._verify_img, data['CodeNumberTextBox'], self._save_path)
        if self._login_status is False:
            print("登录失败")

    def getOptionsCourse(self):
        """
        获取选修课
        :return: course dict
        """
        if self._login_status is False:
            return None

        headers = self._getHeaders()
        views = self._session.get(self._course_view_url, headers=headers)
        tree = etree.HTML(views.text)
        courses_list = self._getOptionsList(tree)
        return self._OptionsListToDict(courses_list)

    def _saveLoginSuccessVerifyCode(self, img: bytes, verify_code, save_path):
        """
        保存验证码图片以及验证码
        :param img: image bytes
        :param verify_code: success verify code
        :param save_path: save verify image path
        :return:
        """
        if os.path.isdir("{}/{}".format(save_path, "verifyImg")) is False:
            os.mkdir("{}/{}".format(save_path, "verifyImg"))
        with open("{}/{}/{}.png".format(save_path, "verifyImg", verify_code), 'wb') as f:
            f.write(img)

    def _getHeaders(self, Referer=None):
        """
        获取session cookie并加入headers中
        :return: headers
        """

        headers = self._headers.copy()
        cookies = self._session.cookies.get_dict()
        self._cookie.update(cookies)
        cookie = ''
        for key in self._cookie.keys():
            cookie += '{0}={1};'.format(key, self._cookie[key])
        headers["cookie"] = cookie
        if Referer is not None:
            headers["Referer"] = Referer
        return headers

    def _getOptionsList(self, tree):
        """
        获取课程list [[course info]...]
        :param tree: HTML TREE
        :return: list -> [[course info]...]
        """
        tr = tree.xpath('//table[@id="{}"]/*'.format("grdRandSchedule"))[1:]
        result = []
        for t in tr:
            fonts = t.xpath('*/font')
            result.append(["".join(str(font.text).split()) for font in fonts])
        return result

    def _OptionsListToDict(self, course_list):
        """
        格式化课程List 转换为字典
        :param course_list: [[course info]...]
        :return: course dict
        """
        re_dict = tree()
        re_dict.update({
            "course": {}
        })

        for course in course_list:
            base_dict = {
                "course": course[1],
                "day": self.MAP_DAYS[course[2]],
                "teacher": course[6],
                "location": course[5],
                "remark": course[8]
            }
            node_str = str(course[3]).replace("节", "")
            node = node_str.split(",")
            node = [int(n) for n in node]

            week_str = str(course[4]).replace("周", "")
            week = week_str.split("，")
            week = [w for w in week]
            week_num = []
            for w in week:
                num = w.split('-')
                week_num.extend([i for i in range(int(num[0]), int(num[1]) + 1)])

            for w in week_num:
                re_dict["course"]["week{}".format(w)] = []
                for n in node:
                    base = base_dict.copy()
                    base["node"] = n
                    re_dict["course"]["week{}".format(w)].append(base)

        return re_dict

    def _match_tag_value_by_name(self, tree, tag_type, name):
        """
        获取文档中指定标签
        :param tree:
        :param tag_type:
        :param name:
        :return:
        """
        xpath = '//{}[@name="{}"]/@value'.format(tag_type, name)
        return tree.xpath(xpath)[0]
