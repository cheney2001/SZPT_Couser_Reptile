# szpt-course-reptile

根据学院班级批量查询深职院全校课表模块，可单独查询选修课表。

## 安装 & 使用

#### 必备条件
* Chrome 
* Chrome Driver
* Python 3.6+

### 安装

```shell script
    pip install szpt-course-reptile
```

##### whl 安装 

``` shell script
    pip install szpt_course_reptile-0.0.1-py3-none-any.whl
```

### Example

##### 查询所有课表

```
    from szpt_course_base.ClassQuery import ClassQuery, BrowsProcess
    college_class_dict = ClassQuery.get_college_class_dict("课表域名")
    process = BrowsProcess(college_class_dict, 4, "jw.szpt.edu.cn")
    result = process.getCourse()
```

##### 查询某一个学院的所有班级课表

```
    from szpt_course_base.ClassQuery import ClassQuery, BrowsProcess
    college_class_dict = ClassQuery.get_college_class_dict("课表域名")
    process = BrowsProcess({"人工智能学院" : college_class_dict["人工智能学院"]}, 4, "课表域名")
    result = process.getCourse()
```

##### 选修课查询

> 具有一个可选保存识别成功的验证码参数 save_verify_img_path 

```
    course = CourseOptions(API_KEY='百度开放平台API—KEY', Secret_Key='百度开放平台Secret_Key',
                           host_name='课表域名')
    course.login("you number", "you password")
    option_course = course.getOptionsCourse()
```

