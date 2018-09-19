# coding=utf8
import os           # 操作系统相关的模块
import time         # 用来获取时间和处理时间的模块
import datetime     # 专门用来获取日期的模块
import shutil       # 文件操作的模块

'''将指定目录下的文件，按照最后修改日期，根据条件(是否在一周之内修改过)归类到new和old两个文件夹内'''

# 要处理的路径
source_dir = u"E:/temp"

# 创建new目录
new_dir = os.path.join(source_dir, 'new')
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

# 创建old目录
old_dir = os.path.join(source_dir, 'old')
if not os.path.exists(old_dir):
    os.makedirs(old_dir)

# 分类条件, 一周前的日期
condition = datetime.date.today() + datetime.timedelta(days=-7)
# 将时间格式化为时间戳用于计算
format_condition = time.mktime(condition.timetuple())

for file_name in os.listdir(source_dir):
    # 获取文件完整路径
    source_path = os.path.join(source_dir, file_name)
    if os.path.isfile(source_path):
        # 获取文件修改时间
        modify_time = os.path.getmtime(source_path)
        # 是否在一周之内修改过
        if modify_time > format_condition:
            # 如果修改过，将文件移动到new_dir
            target_path = os.path.join(new_dir, file_name)
        else:
            # 如果没有修改过，将文件移动到old_dir
            target_path = os.path.join(old_dir, file_name)
        shutil.move(source_path, target_path)
