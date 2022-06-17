import setuptools

#
# with open('README.md', 'r', encoding='utf-8') as fh:
#     long_description = fh.read()

setuptools.setup(
    # 包名称
    name='compilet',
    version='0.0.2',
    author='ygg',
    author_email='ygg@zut.edu.cn',
    description='Oh Bear !',
    # long_description=long_description,

    # 包上传到pypi的对应目录
    # url='https://gitee.com/ly_love_ly/xiaoxiong',
    # 打包时开始目录
    packages=setuptools.find_packages(''),
    # package_dir = {"":"compile"},		# 告诉 setuptools 包都在 qiye 下
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

