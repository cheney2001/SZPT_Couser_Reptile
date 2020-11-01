from szpt_course_option.courseOption import CourseOptions
import collections
import json

tree = lambda: collections.defaultdict(tree)

if __name__ == "__main__":
    course = CourseOptions(API_KEY='3uCM2HafGbKma7DIQgAkIzVB', Secret_Key='XkrS0153qKY3PmETZN9KmbIQAeQgf9b0',
                           host_name='jwgl.szpt.edu.cn')
    course.login("19240302", "li745789")
    option_course = course.getOptionsCourse()
    print(json.dumps(option_course, ensure_ascii=False))
