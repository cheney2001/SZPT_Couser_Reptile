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
    def _matchCourse(driver: WebDriver):
        """
        匹配并处理课程表
        :param driver:
        :return:
        """
        rows = driver.find_elements_by_xpath('//table[@id="gvSchedule"]/tr')[1:]
        for row in rows :
            ths = row.find_elements_by_xpath('/th')
            course_type = ths[0].text
            course_class = ths[1].text
            course_name = ths[2].text
            course_teacher1 = ths[3].text
            course_teacher2 = ths[4].text
            course_week = ths[5].text
            course_location = ths[6].text
            course_day = ClassQuery.MAP_DAYS[ths[7].text]
            course_node = ths[8].text
            course_remarks = ths[9].text


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
