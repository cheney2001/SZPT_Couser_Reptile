from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from szpt_course.course import *
import collections

tree = lambda: collections.defaultdict(tree)


class ClassQuery:
    """
    查询全校所有班级的课表
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

    def __init__(self):
        # 配置为无头模式
        self._ch_options = Options()
        self._ch_options.add_argument("--headless")
        self._ch_options.add_argument('--disable-gpu')
        self._ch_options.add_argument('--window-size=1366,768')
        self._driver = webdriver.Chrome(chrome_options=self._ch_options)

    def _getIndex(self):
        self._driver.get("http://jw.szpt.edu.cn/kb/WebKb/Kbcx.aspx")

    def _getCollegeList(self):
        self._getIndex()
        options = self._driver.find_elements_by_xpath('//select[@id="ddlAcademy"]/option')[1:]
        college_list = [
            (opt.text, opt.get_attribute("value"))
            for opt in options
            if "学院" in opt.text
        ]
        return college_list

    def _getClassList(self, colleges):
        result = {}
        for college in colleges:
            self._driver.find_element_by_xpath(
                '//select[@id="ddlAcademy"]/option[@value="{}"]'.format(college[1])).click()
            options = self._driver.find_elements_by_xpath('//select[@id="ddlClass"]/option')[1:]
            result[college[0]] = [(opt.text, opt.get_attribute("value")) for opt in options]
        return result

    def _getCourse(self, college_list, class_list):
        course = tree()
        for college in college_list:
            self._driver.find_element_by_xpath(
                '//select[@id="ddlAcademy"]/option[@value="{}"]'.format(college[1])).click()
            classes = class_list[college[0]]
            for class_ in classes:
                self._driver.find_element_by_xpath(
                    '//select[@id="ddlClass"]/option[@value="{}"]'.format(class_[1])).click()
                self._driver.find_element_by_xpath('//input[@id="btnClass"]').click()
                page = str(self._driver.page_source)
                course[college[0]][class_[0]] = self._matchCourse(driver=self._driver)
        return course

    @staticmethod
    def _format_week(course_week: str):
        """
        处理周次字串
        example : 1-4，8-12，15-16周
        :param course_week: 周次字串
        :return: week list
        """
        if course_week == '' or course_week == ' ' or course_week == None:
            return None
        course_week = course_week.replace("周", '')
        week_str_list = course_week.split('，')
        week = []
        for week_str in week_str_list:
            if '-' not in week_str:
                week.append(int(week_str))
                continue
            start, end = week_str.split('-')
            week.extend([i for i in range(int(start), int(end) + 1)])
        return week

    @staticmethod
    def _format_node(course_node: str):
        """
        处理节次字串
        example :  1,2节
        :param course_node: 节次字段
        :return: node list
        """
        if course_node == '' or course_node == ' ' or course_node == None:
            return None
        course_node = course_node.replace('节', '')
        start, end = course_node.split(',')
        return [i for i in range(int(start), int(end) + 1)]

    @staticmethod
    def _comp_bottom_table_rows(bottom_table_rows: list):
        """
        处理整周的表内行元素
        :param bottom_table_rows:
        :return:
        """

        def default(col: dict, idx: str, value):
            if value == '' or value == ' ' or value is None:
                pass
            else:
                col[idx] = value

        example = {
            "type": '',
            "name": '',
            "teacher_main": '',
            "teacher_ass": '',
            "location": '',
            "day": '',
            "remarks": '',
        }
        example_copy = example.copy()
        for row in bottom_table_rows:
            ths = row.find_elements_by_xpath('/td')
            default(example, 'type', ths[0].text)
            default(example,'name')

    @staticmethod
    def _format_course_rows(top_table_rows: list, bottom_table_rows: list = None):
        """
        处理课表tr 行元素
        :param top_table_rows: 班级课表元素List
        :param bottom_table_rows: 整周课表元素List
        :return:
        """
        for row in top_table_rows:
            ths = row.find_elements_by_xpath('/td')
            course_dict = tree()
            # 周次
            course_week = ths[5].text
            course_week = ClassQuery._format_week(course_week=course_week)
            # 节次
            course_node = ths[8].text
            course_node = ClassQuery._format_node(course_node=course_node)
            # 班级
            classes = ths[1].text
            course_dict[classes] = tree()
            example = {
                "type": ths[0].text,
                "name": ths[2].text,
                "teacher_main": ths[3].text,
                "teacher_ass": ths[4].text,
                "location": ths[6].text,
                "day": ClassQuery.MAP_DAYS[ths[7].text],
                "remarks": ths[9].text,
            }
            if example["type"] == "":
                for week in course_week:
                    for node in course_node:
                        if "week{}".format(str(week)) not in course_dict[classes].keys():
                            course_dict[classes]["week{}".format(str(week))] = []
                        example["node"] = node
                        course_dict[classes]["week{}".format(str(week))].append(example)
            elif example["type"] == "整周":
                pass

    @staticmethod
    def _matchCourse(driver: WebDriver):
        """
        匹配并处理课程表
        :param driver:
        :return:
        """
        rows = driver.find_elements_by_xpath('//table[@id="gvSchedule"]/tr')[1:]


if __name__ == "__main__":
    # course_obj = Course('jw.szpt.edu.cn')
    # course_obj.query("19240308")

    c = ClassQuery()
    colleges = c._getCollegeList()
    # c._getClassList(colleges)
    class_list = c._getClassList(colleges)
    print(colleges)
    print(class_list)
    c._getCourse(colleges, class_list)
