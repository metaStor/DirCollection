# !/usr/bin/env python
# encoding  : utf-8
# @Time     : 2020/6/20 12:35 
# @Author   : metaStor
# @File     : parse_dir.py
# @Desc     : 解析网站目录，去重，生成唯一的字典集合，写入原始字典中（排重）


import os
import sys
import getopt


def file_name(file_dir):
    dirs = []
    for root, dir, files in os.walk(file_dir):
        # print('root_dir:', root)  # 当前目录路径
        # print('sub_dirs:', dirs)  # 当前路径下所有子目录
        # 目录后面加/
        dir = [x+'/' for x in dir]
        dirs += dir
        # print('files:', files)  # 当前路径下所有非目录子文件
        dirs += files
    return dirs  # 无重复项


def create_file(filename):
    """
    创建文件夹和文件
    """
    path = filename[0:filename.rfind("/")]
    if not os.path.isdir(path):  # 无文件夹时创建
        os.makedirs(path)
    if not os.path.isfile(filename):  # 无文件时创建
        fd = open(filename, mode="w", encoding="utf-8")
        fd.close()
    else:
        pass


# 写入自己收集的字典中
def write_dict(dirs, dict_name):

    # 输出文件不存在就创建一个新的
    create_file(dict_name)

    with open(dict_name, 'r') as f1:
        content = f1.read().split()

    with open(dict_name, 'a+') as f2:
        for file in dirs:
            if len(content) <= 0 or file not in content:
                f2.write(file + '\n')
    return True


if __name__ == '__main__':
    argv = sys.argv[1:]
    dir, file = '', ''

    try:
        opts, args = getopt.getopt(argv, "hd:f:", ["help", "dir=", "file="])
    except getopt.GetoptError:
        print('parse_dir.py -d <dir> -f <file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('parse_dir.py -d <dir> -f <file>')
            sys.exit(-1)
        elif opt in ("-d", "--dir"):
            dir = arg
        elif opt in ("-f", "--file"):
            file = arg

    if dir == '' or file == '':
        print('parse_dir.py -d <dir> -f <file>')
        sys.exit(-2)

    dirs = file_name(dir)
    if write_dict(dirs, file):
        print('[*] Complete! Added %d dirs' % len(dirs))
