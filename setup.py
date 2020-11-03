import setuptools

setuptools.setup(
    name="szpt_course_reptile",
    version="0.0.1",
    author="Cheney",
    author_email="cheney2001@qq.com",
    description="use for get szpt course and option course",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests==2.24.0",
        "lxml==4.6.1",
        "numpy==1.19.4",
        "selenium==3.141.0",
    ]
)
