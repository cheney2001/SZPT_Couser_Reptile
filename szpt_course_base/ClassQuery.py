from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
import collections
import json
import re
from multiprocessing import Pool

tree = lambda: collections.defaultdict(tree)


class ClassQuery:
    """
    查询全校所有班级的课表
    return course :
        {
            "semester": "2020-2021学年第一学期",
            "date_time": "第8周",
            "week_int": "星期五",
            "is_start": "",
            "学院名称":{
                "班级简称":{
                    "week1":[
                            {
                            "type": "课程类型",
                            "name": "课程名称",
                            "teacher_main": "主讲教师",
                            "teacher_ass": "辅助教师",
                            "location": "上课地点",
                            "day": 2(星期几),
                            "remarks": "备注",
                            "node": 2 (第几节课)
                        },
                        ...
                    ]
                }
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

    def __init__(self, host_name: str):
        # 配置为无头模式
        self._ch_options = Options()
        self._ch_options.add_argument("--headless")
        self._ch_options.add_argument('--disable-gpu')
        self._ch_options.add_argument('--window-size=1366,768')
        self._driver = webdriver.Chrome(chrome_options=self._ch_options)
        self.host_name = host_name
        self._getIndex()

    def _getIndex(self):
        self._driver.get("http://{}/kb/WebKb/Kbcx.aspx".format(self.host_name))

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

    def getCourse(self, college_class_dict: dict):
        course = tree()
        for college in college_class_dict.keys():
            self._driver.find_element_by_xpath(
                '//select[@id="ddlAcademy"]/option[@value="{}"]'.format(college_class_dict[college]['code'])).click()
            classes = college_class_dict[college]["class"]
            for class_ in classes:
                self._driver.find_element_by_xpath(
                    '//select[@id="ddlClass"]/option[@value="{}"]'.format(class_[1])).click()
                self._driver.find_element_by_xpath('//input[@id="btnClass"]').click()
                page = str(self._driver.page_source)
                result = self._matchCourse(driver=self._driver)
                if result is None or len(result) == 0:
                    continue
                course[college][class_[0]] = result["course"].copy()
                course["semester"] = result["semester"]
                course["date_time"] = result["week_str"]
                course["week_int"] = result['day']
                course["is_start"] = result['is_start']
                # print(json.dumps(result, ensure_ascii=False))
        return course

    def close(self):
        self._driver.close()

    @staticmethod
    def get_college_class_dict(host_name: str) -> dict:
        """
        返回学院-班级的查询参数字典
        :return: query dict
        """
        browser = ClassQuery(host_name)
        browser._getIndex()
        colleges = browser._getCollegeList()
        browser._getClassList(colleges)
        class_list = browser._getClassList(colleges)
        college_class_dict = browser._merge_college_class(colleges, class_list)
        browser._driver.close()
        return college_class_dict

    @staticmethod
    def _merge_college_class(college_list: list, class_dict: dict) -> dict:
        """
        合并年级和班级列表
        :param college_list:
        :param class_dict:
        :return:
        """
        for college in college_list:
            name, code = college
            classes = class_dict[name]
            class_dict[name] = {
                "class": classes,
                "code": code
            }
        return class_dict.copy()

    @staticmethod
    def _format_week(course_week: str):
        """
        处理周次字串
        example : 1-4，8-12，15-16周
        example : [1-9]单周
        example : 第6周
        example : （2-10）双周
        :param course_week: 周次字串
        :return: week list
        """

        def format_single_week(course_week: str):
            # 处理单周情况
            week = []
            single_week_list = re.findall('(?<=\\[)[^\\]]+', course_week)
            for single_week in single_week_list:
                start, end = str(single_week).split('-')
                week.extend([i for i in range(int(start), int(end) + 1) if i % 2 != 0])
            return (week, course_week)

        def format_double_week(course_week: str):
            # 处理双周的情况
            week = []
            double_week_list = re.findall('(?<=\\（)[^\\）]+', course_week)
            for double_week in double_week_list:
                start, end = str(double_week).split('-')
                week.extend([i for i in range(int(start), int(end) + 1) if i % 2 == 0])

            return (week, course_week)

        if course_week == '' or course_week == ' ' or course_week == None:
            return None
        week = []
        while '单周' in course_week or '双周' in course_week:
            str_split = course_week.split('，')
            for str_ in str_split:
                if '单周' in str_:
                    single_week, _ = format_single_week(str_)
                    week.extend(single_week)
                    course_week = course_week.replace(str_, '')
                elif '双周' in str_:
                    double_week, _ = format_double_week(str_)
                    week.extend(double_week)
                    course_week = course_week.replace(str_, '')

        course_week = course_week.replace("周", '')
        course_week = course_week.replace("第", '')
        week_str_list = course_week.split('，')

        for week_str in week_str_list:
            if week_str == '' or week_str == ' ':
                continue
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
        example :  1,2节 or 1-4节
        :param course_node: 节次字段
        :return: node list
        """
        if course_node == '' or course_node == ' ' or course_node == None:
            return None
        course_node = course_node.replace('节', '')
        course_node = course_node.replace('第', '')
        if ',' in course_node:
            # 5,6,7节
            node_list = course_node.split(',')
            return [int(i) for i in node_list]
        elif '-' in course_node:
            # 1-4节
            start, end = course_node.split('-')
            return [i for i in range(int(start), int(end) + 1)]
        else:
            # 第4节
            return [int(course_node)]

    @staticmethod
    def _comp_bottom_table_rows(bottom_table_rows: list):
        """
        处理整周的表内行元素
        :param bottom_table_rows:
        :return:
        """
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
        course_name_rows = []
        course_info_rows = []
        for row in range(len(bottom_table_rows)):
            tds = bottom_table_rows[row].find_elements_by_xpath('td')
            type = str(tds[0].text)
            if type != ' ':
                course_name_rows.append(tds)
                course_info_rows.append([])
            else:
                course_info_rows[len(course_info_rows) - 1].append(tds)
        course_dict = tree()
        for title, course in zip(course_name_rows, course_info_rows):
            example = example_copy.copy()
            example["type"] = ClassQuery.del_space(title[0].text)
            example["name"] = ClassQuery.del_space(title[2].text)
            for course_ in course:
                day = ClassQuery.MAP_DAYS[course_[7].text] if ClassQuery.del_space(course_[7].text) != '' else ''
                location = ClassQuery.del_space(course_[6].text) if ClassQuery.del_space(
                    course_[6].text) != '' else "待定"
                example["teacher_main"] = ClassQuery.del_space(course_[3].text)
                example["teacher_ass"] = ClassQuery.del_space(course_[4].text)
                example["remarks"] = ClassQuery.del_space(course_[9].text)
                example["location"] = location
                example["day"] = day
                node = ClassQuery._format_node(course_[8].text)
                week = ClassQuery._format_week(course_[5].text)
                week_key = "week{}".format(str(week[0]))
                if week_key not in course_dict.keys():
                    course_dict[week_key] = []
                if node is None:
                    course_dict[week_key].append(example.copy())
                    continue
                for n in node:
                    example["node"] = n
                    course_dict[week_key].append(example.copy())
        return course_dict

    @staticmethod
    def del_space(value):
        if value == ' ' or value is None:
            return ''
        else:
            return value

    @staticmethod
    def _format_course_rows(top_table_rows: list, bottom_table_rows: list = None):
        """
        处理课表
        :param top_table_rows: 班级课表元素List
        :param bottom_table_rows: 整周课表元素List
        :return:
        """

        course_dict = tree()

        for row in top_table_rows:
            ths = row.find_elements_by_xpath('td')
            # 过滤掉非一般课程：如 （单元，整周）
            type = str(ths[0].text)
            if type != ' ' and type != '拓展':
                continue
            # 周次
            course_week = ths[5].text
            course_week = ClassQuery._format_week(course_week=course_week)
            # 节次
            course_node = ths[8].text
            course_node = ClassQuery._format_node(course_node=course_node)
            day = ClassQuery.del_space(ths[7].text)
            example = {
                "type": ClassQuery.del_space(type),
                "name": ClassQuery.del_space(ths[2].text),
                "teacher_main": ClassQuery.del_space(ths[3].text),
                "teacher_ass": ClassQuery.del_space(ths[4].text),
                "location": ClassQuery.del_space(ths[6].text) if ClassQuery.del_space(ths[6].text) != '' else "待定",
                "day": ClassQuery.MAP_DAYS[day] if day != '' else '',
                "remarks": ClassQuery.del_space(ths[9].text),
            }

            for week in course_week:
                week_key = "week{}".format(str(week))
                if week_key not in course_dict.keys():
                    course_dict[week_key] = []
                if course_node is None:
                    # 主课表节次可能为空
                    course_dict[week_key].append(example.copy())
                    continue
                for node in course_node:
                    example["node"] = node
                    course_dict[week_key].append(example.copy())
        # print(json.dumps(course_dict, ensure_ascii=False))
        if bottom_table_rows is not None:
            result = ClassQuery._comp_bottom_table_rows(bottom_table_rows=bottom_table_rows)
            for week in result.keys():
                if week not in course_dict.keys():
                    course_dict[week] = []
                course_dict[week].extend(result[week])
        return course_dict

    @staticmethod
    def _matchCourse(driver: WebDriver):
        """
        匹配并处理课程表
        :param driver:
        :return:
        """

        def func_handle(func, arg, default=None):
            try:
                result = func(arg)
                return result
            except:
                return default

        def get_top_table(driver):
            return driver.find_elements_by_xpath('//table[@id="gvSchedule"]//tr')[1:]

        def get_bottom_table(driver):
            return driver.find_elements_by_xpath('//table[@id="gvScheduleAllWeek"]//tr')[1:]

        def get_semester(driver: WebDriver):
            """
            获取学年和学期信息
            :param driver:
            :return:
            """
            title = driver.find_element_by_id("lXqInfo").text
            [semester] = re.findall('深圳职业技术学院课表查询系统\((.*?)\)', title)
            return semester

        def get_week_info(driver: WebDriver):
            """
            获取元素
            :param driver:
            :return:
            """
            title = driver.find_element_by_id("Rq").text
            [week_info] = re.findall('今天是(\d+-\d+-\d+)\s*(第(\d+)周)?\s*(星期.)\s*(\(未开学\))?', title)
            return week_info

        top_table_rows = func_handle(get_top_table, driver)
        bottom_table_rows = func_handle(get_bottom_table, driver)
        if top_table_rows is None and bottom_table_rows is None:
            return None
        semester = func_handle(get_semester, driver)
        date_time, week_str, week_int, day, is_start = get_week_info(driver)
        course_dict = ClassQuery._format_course_rows(top_table_rows, bottom_table_rows)

        result = {
            "semester": semester,
            "date_time": date_time,
            "week_str": week_str,
            "week_int": int(week_int),
            "day": day,
            "is_start": is_start,  # 是否开学
            "course": course_dict,
        }
        return result


class BrowsProcess:
    """
    开启多进程爬取课表 , 再开启多线程时请勿过多( process_num < CPU 核心数)
    course =
        {
            "semester": "2020-2021学年第一学期",
            "date_time": "第8周",
            "week_int": "星期五",
            "is_start": "",
            "学院名称":{
                "班级简称":{
                    "week1":[
                            {
                            "type": "课程类型",
                            "name": "课程名称",
                            "teacher_main": "主讲教师",
                            "teacher_ass": "辅助教师",
                            "location": "上课地点",
                            "day": 2(星期几),
                            "remarks": "备注",
                            "node": 2 (第几节课)
                        },
                        ...
                    ]
                }
            }
        }
    :return [('学院名称' , course), ...]
    """

    def __init__(self, college_class_dict: dict, process_num: int, host_name: str):
        """
        初始化多进程爬虫对象
        :param college_class_dict: 学院-班级 json
        :param process_num: 并行进程数
        """
        self.college_class_dict = college_class_dict
        self.process_num = process_num
        self.host_name = host_name

    def getCourse(self):
        """
        获取self.college_class_dict 中所包含的学院以及班级的课表
        :return: [("college_name" , course_json),...]
        """
        pool = Pool(processes=self.process_num)
        process_list = []
        for key in self.college_class_dict.keys():
            arg_dict = {key: self.college_class_dict[key]}
            process_list.append(pool.apply_async(BrowsProcess._getCourse, (arg_dict, key, self.host_name)))
        pool.close()
        pool.join()
        return [pro.get() for pro in process_list]

    @staticmethod
    def _getCourse(college_class_dict: dict, key, host_name):
        """
        返回课表Json 字串与学院名称元组
        :param college_class_dict: college and classes dict
        :param key: college name
        :param host_name: course site host name
        :return: (college_name , course_json_str)
        """
        brows = ClassQuery(host_name)
        result = brows.getCourse(college_class_dict)
        print("college : {} course get success".format(key))
        brows.close()
        result = json.dumps(result, ensure_ascii=False)
        return (key, result)
