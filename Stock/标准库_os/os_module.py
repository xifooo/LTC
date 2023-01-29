#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   os_module.py
@Time    :   2022/11/08 16:44:20
'''
import os


introduction = "os模块的主要功能: 系统相关、目录及文件操作、执行命令和管理进程"

def system_related():
    info = {}
    
    info[r"os.name: 当前系统名字"] = f"{os.name}"
    
    info["os.environ: 系统环境变量"] = f"{os.environ}"
    info["os.pathsep: 系统PATH环境变量中的分隔符"] = f"{os.pathsep}"
    
    info["os.sep: 当前系统的路径分隔符"] = f"{os.sep}"
    # info["当前系统的可替代路径分隔符: os.altsep"] = os.altsep
    info["os.extsep: 文件名和文件扩展名之间分隔的符号"] = f"{os.extsep}"
    
    info["os.linesep: 行尾的行结束符"] = f"{os.linesep}"
    
    info["os.devnull: null设备的路径"] = f"{os.devnull}"
    # info["当使用exec函数族的时候, 如果没有指定PATH环境变量, 则默认会查找os.defpath中的值作为子进程PATH的值。"] = os.defpath
    return info


def file_dir_related():
    info = {}
    # 查 - 文件、目录(即路径、文件夹)
    info["os.getcwd(): 当前python脚本工作的目录"] = f"{os.getcwd()}"
    info["os.listdir('dir_name'): 列出指定目录下的所有文件和子目录, 包括隐藏文件"] = "os.listdir(os.getcwd())"
    info["os.stat('path/file_name'): 获取文件/目录信息"] = "os.stat(f'{os.getcwd()/main.py}'"
    # info["当前目录, 即'.'_os.curdir"] = os.curdir
    # info["当前目录的父级目录字符串名, 即'..'_os.pardir"] = os.pardir
    
    # 增 
    info["os.mkdir('dir_name'): 在当前工作目录下, 生成一个目录"] = "os.mkdir()"
    info["os.makedirs('d_1/d_2'): 在当前工作目录下, 生成多层递归目录"] = "os.makedirs('first/good')"
    
    # 删
    info["os.rmdir('dir_name'): 删除一个空目录"] = "os.rmdir('first')"
    info["os.removedirs('dir_1/dir_2'): 递归删除空目录"] = "os.removedirs('first')"

    info["os.remove('file_name'): 删除一个文件"] = "os.remove('demo.py')"
    
    # 改
    info["os.chdir('dir_name'): 改变当前脚本工作目录_相当于shell里的cd操作"] = "os.chdir('F:\下载\Compressed')"
    info["os.rename('Old_name','New'): 重命名文件或目录"] = "os.rename('demo.py', 'main.py')"
    # os.chmod()
    
    # 切割与拼接
    info["os.path.abspath(os.curdir): 规范化的绝对路径_效果相当于os.getcwd()"] = f"{os.path.abspath(os.curdir)}"
    info["os.path.split(os.getcwd()): 将path分割为目录与文件名/文件夹名二元组并返回"] = f"{os.path.split('{os.curdir}/main.py')}"
    info["os.path.dirname(path): 返回path的目录。其实就是os.path.split(path)的第一个元素"] = f"{os.path.dirname(os.getcwd())}"
    info["os.path.basename(path): 返回path最后的文件名。如果path以/或\结尾, 那么就会返回空值。"] = f"{os.path.basename(os.getcwd())}"

    # 判断
    info["os.path.exists(path或file): 如果path存在, 返回True; 如果path不存在, 返回False"] = "{os.path.exists('F:\\myWS\\first')}"
    info["os.path.isabs(path): 判断path是一个绝对路径"] = "os.path.isabs('F:\\myWS\\first')"
    info["os.path.isfile(path): 判断path是一个存在的文件"] = "os.path.isfile('F:\\myWS\\first')"
    info["os.path.isdir(path): 判断path是一个存在的目录"] = "os.path.isdir('F:\\myWS\\first')"
    info["os.path.join(path,*path): 智能地拼接一个或多个路径部分, 并返回"] = "os.path.join(os.getcwd(),'test.py')"
    info["os.path.getatime(path): 返回path所指向的文件或者目录的最后存取时间"] = "os.path.getatime(os.getcwd())"
    info["os.path.getmtime(path): 返回path所指向的文件或者目录的最后修改时间"] = "os.path.getmtime(os.getcwd())"
    info["os.path.getsize(filename): 返回文件包含的字符数量"] = "os.path.getsize('F:\\myWS\\main.py')"
    return info

class Walk:
    def __init__(self) -> None:
        self.info = {}
        self.info["os.walk(top, topdown=True, onerror=None, followlinks=False): \
        生成一个三元组 (dirpath, dirnames, filenames)"] = "os.walk(os.getcwd(),topdown=True,"
        """
        dirpath 是表示目录路径的字符串
        dirnames 是 dirpath 中子目录名称组成的列表 (excluding '.' and '..')
        filenames 是 dirpath 中非目录文件名称组成的列表。"""
        
        """ https://docs.python.org/zh-cn/3.9/library/os.html?highlight=os%20walk#os.walk """
        
    @staticmethod
    def walk_test_one():
        description = "将c:\python36目录中的所有文件和子目录打印出来"
        try:
            for root, dirs, files in os.walk(r"c:\python36"):
                print("\033[1;31m-"*8, "directory", "<%s>\033[0m" % root, "-"*10)
                for directory in dirs:
                    print("\033[1;34m<DIR>    %s\033[0m" % directory)
                for file in files:
                    print("\t\t%s" % file)
            print(description)
        except OSError as ex:
            print(ex)
    
    @staticmethod
    def walk_test_two():
        description = "统计c:/python36/Lib/email目录下所有子目录的大小, 但是CVS目录除外。"
    
        for root, dirs, files in os.walk('c:/python36/Lib/email'):
            print(root, "consumes", end=" ")
            print(sum(os.path.getsize(os.path.join(root, name)) for name in files), end=" ")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # 不遍历CVS目录
        print(description)
    
    @staticmethod
    def walk_test_three():
        description = "递归删除目录的所有内容，危险，请勿随意尝试！"
        
        print(description)
        
        fix = input("are you sure? Y/N")
        if fix.lower() == "y":
            for root, dirs, files in os.walk("c:/python36/Lib/email", topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
        else:
            return 0

def main():
    info = {}

    info["os.cup_count: 当前计算机的核心数"] = f"{os.cpu_count}"
    info["os.system和popen可执行系统命令"] = "os.system(command), ret = os.popen(command, [mode, [bufsize]])"
    
    sys_info = system_related()
    file_dir_info = file_dir_related()
    info = {**sys_info, **file_dir_info}
    return info


if __name__ == "__main__":
    info = main()
    import json, pathlib
    curdir = pathlib.Path(__file__).parent
    name = pathlib.Path(__file__).stem
    with open(f"{curdir}/{name}.json", "w") as f:
        f.write(json.dumps(info, 
                           indent=4,
                           ensure_ascii=False))
    
