from setuptools import setup, find_packages

setup(
    name='pypalan',
    version='0.0.1',
    description='python palan read data',
    author='yuanzhencai',
    author_email='zhencai.yuan@datarx.cn',
    tests_require=[
      'unittest2',
    ],
    test_suite='unittest2.collector',
    packages=['pypalan'],
    install_requires=[
      'pyodbc',
      'pandas'
    ]
)
