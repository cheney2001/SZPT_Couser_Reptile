from szpt_course_option.courseOption import CourseOptions
import collections

tree = lambda: collections.defaultdict(tree)

if __name__ == "__main__":
    course = CourseOptions()
    course.login("19240308", "zse55667788")
    option_course = course.getOptionsCourse()
    print(option_course)
