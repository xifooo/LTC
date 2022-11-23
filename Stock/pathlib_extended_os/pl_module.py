#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   pathlib.py
@Time    :   2022/11/09 18:21:32
'''
# from pathlib import Path, PurePosixPath, PureWindowsPath
import os, pathlib


def file_dir_related():
    info = {}
    # 查 - 文件、目录(即路径、文件夹)
    info["os.getcwd(): 当前python脚本工作的目录"] = os.getcwd()
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
    
    # 切割与拼接
    info["os.path.abspath(os.curdir): 规范化的绝对路径_效果相当于os.getcwd()"] = os.path.abspath(os.curdir)
    info["os.path.split(os.getcwd()): 将path分割为目录与文件名/文件夹名二元组并返回"] = os.path.split(f'{os.curdir}/main.py')
    info["os.path.dirname(path): 返回path的目录。其实就是os.path.split(path)的第一个元素"] = os.path.dirname(os.getcwd())
    info["os.path.basename(path): 返回path最后的文件名。如果path以/或\结尾, 那么就会返回空值。"] = os.path.basename(os.getcwd())

    # 判断
    info["os.path.exists(path或file): 如果path存在, 返回True; 如果path不存在, 返回False"] = os.path.exists('F:\\myWS\\first')
    info["os.path.isabs(path): 判断path是一个绝对路径"] = os.path.isabs('F:\\myWS\\first')
    info["os.path.isfile(path): 判断path是一个存在的文件"] = os.path.isfile('F:\\myWS\\first')
    info["os.path.isdir(path): 判断path是一个存在的目录"] = os.path.isdir('F:\\myWS\\first')
    info["os.path.join(path,*path): 智能地拼接一个或多个路径部分, 并返回"] = os.path.join(os.getcwd(),'test.py')
    info["os.path.getatime(path): 返回path所指向的文件或者目录的最后存取时间"] = os.path.getatime(os.getcwd())
    info["os.path.getmtime(path): 返回path所指向的文件或者目录的最后修改时间"] = os.path.getmtime(os.getcwd())
    info["os.path.getsize(filename): 返回文件包含的字符数量"] = "os.path.getsize('F:\\myWS\\main.py')"
    return info

def pl_related():
    # tmp = Path.cwd()  # 目录
    tmp = pathlib.Path(__file__)   # 文件路径
    
    # 读写文件
    f = pathlib.Path("f:\myWS\ifmain.py")
    # f.write_text("test_text_pathlib = 'just a test text'")   # 覆盖性写入
    f.read_text()
    # with f.open() as f: f.readline()
    
    # 查
    print(tmp)
    print(list(tmp.iterdir())) # == os.listdir(tmp)
    print(list(tmp.glob("*.py"))) # 通配符, os不支持
    # 目录或文件路径的元数据
    print(f"目录或文件路径的详细信息(同os.stat): {f.stat()}")
    print(f"原子化切割目录或文件路径信息(路径的多个组件): {f.parts}")
    print(f"目录或文件路径的完整信息: {f.resolve()}")
    print(f"目录或文件路径所在的父级目录: {f.parent}")
    print(f"目录或文件路径的所有者: {f.owner()}")
    print(f"目录或文件路径的所有组: {f.group()}")
    print(f"目录或文件路径的带后缀全名: {f.name}")
    print(f"目录或文件路径的末尾后缀: {f.suffix}")
    print(f"目录或文件路径的所有后缀: {f.suffixes}")
    print(f"目录或文件路径的无后缀名字: {f.stem}")
    print(f"家目录: {f.home()} - {pathlib.Path.home()} - {tmp.home()}")
    
    # 拼接
    print(tmp / "bar")
    print(pathlib.PurePosixPath("/etc").joinpath(pathlib.PurePosixPath("newnew")))
    print(pathlib.PurePosixPath("/etc").joinpath("newnew"))
    print(pathlib.PurePosixPath("/etc").joinpath("newnew", "oldold"))
    print(pathlib.PureWindowsPath('c:').joinpath('/Program Files'))
    # 增
    
    # 删
    
    # 改
    print(tmp.with_name("giogio.py")) # == os.rename
    print(tmp.with_stem("giogio")) # 只修改无后缀文件名的os.rename
    print(tmp.with_suffix(".py")) # 只修改末尾后缀
    
    # 判断
    print(tmp.exists())
    print(tmp.is_dir())
    print(tmp.is_file())
    print(tmp.is_absolute())
    
    # windows与posix风格转化
    p = pathlib.PureWindowsPath('c:\\windows')
    print(p.as_posix())
    # 获取文件的 uri
    print(p.as_uri())
    return 0
    
def main():
    ...


if __name__ == "__main__":
    pl_related()

