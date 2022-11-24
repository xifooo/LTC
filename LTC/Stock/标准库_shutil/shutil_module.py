#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   shutil_module.py
@Time    :   2022/11/19 21:38:13
'''
import shutil


def copy_file(f, g):
    # 可选大小拷贝
    shutil.copyfileobj(fsrc=f, fdst=g, length=16*1024)
    # 完整文件拷贝
    shutil.copyfile(src=f, dst=g)
    # 仅拷贝权限。内容、组、用户均不变。
    shutil.copymode(src=f, dst=g)
    # 仅复制所有的状态信息，包括权限，组，用户，时间等。
    shutil.copystat(src=f, dst=g)
    # 同时复制文件的内容以及权限，也就是先copyfile()然后copymode()。
    shutil.copy(src=f, dst=g)
    # 同时复制文件的内容以及文件的所有状态信息。先copyfile()后copystat()。
    shutil.copy2(src=f, dst=g)
    
    
def operate_dir(f, g):
    # 递归地删除目录及子目录内的文件
    shutil.rmtree()


def main():
    with open("jojo.txt", "r") as f:
        with open("/jojo/main.txt", "w") as g:
            copy_file(f, g)


if __name__ == "__main__":
    main()
