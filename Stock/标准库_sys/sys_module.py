#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   sys_module.py
@Time    :   2022/11/08 16:52:01
'''
import sys

about_sys = "sys模块主要是针对与Python解释器相关的变量和方法, 不是主机操作系统。"

def self_attr_related():
    info = {}
    # python 解释器自身的属性
    info["sys.version: Python解释程器的版本信息"] = f"{sys.version}"
    info["sys.stdin: 输入相关"] = f"{sys.stdin}"
    info["sys.stdout: 输出相关"] = f"{sys.stdout}"
    info["sys.stderr: 错误相关"] = f"{sys.stderr}"
    info["sys.exc_info(): 返回异常信息三元元组"] = f"{sys.exc_info()}"
    info["sys.copyright: 当前Python的版权信息"] = f"{sys.copyright}"
    
    # info["python解释器的首要提示符: sys.ps1"] = sys.ps1
    # info["python解释器的次要提示符: sys.ps2"] = sys.ps2

    info["sys.prefix: python解释器所在目录"] = f"{sys.prefix}"
    return info
    

def system_related():
    info = {}
    # 操作系统相关
    info["sys.path: 返回模块的搜索路径, 初始化时使用PYTHONPATH环境变量的值"] = f"{sys.path}"
    info["sys.maxsize: 最大的Int值, 64位平台是2**63 - 1"] = f"{sys.maxsize}"
    info["sys.getdefaultencoding(): 获取系统当前编码, 默认为utf-8"] = f"{sys.getdefaultencoding()}"
    info["sys.setdefaultencoding(): 设置系统的默认编码"] = "sys.setdefaultencoding()"
    info["sys.getwindowsversion(): 返回当前windwos系统的版本信息"] = f"{sys.getwindowsversion()}"
    return info


def program_related():
    info = {}
    # 程序、环境相关
    info["sys.argv: 命令行参数列表, 第一个元素是程序文件本身(的路径)"] = f"{sys.argv}"
    info["sys.modules: 所有当前Python环境中已经导入的模块(以字典形式)"] = f"{sys.modules}"
    info["sys.builtin_module_names: 所有已经编译到Python解释器里的模块的名字(以列表形式)"] = f"{sys.builtin_module_names}"
    info["sys.getrefcount(object): 返回对象的引用数量"] = f"sys.getrefcount(1) = {sys.getrefcount(1)}"
    info["sys.getrecursionlimit(): 返回Python最大递归深度, 默认1000"] = f"{sys.getrecursionlimit()}"
    info["sys.getsizeof(object[, default]): 返回对象的大小"] = f"sys.getsizeof(1) = {sys.getsizeof(1)}"
    info["sys.getswitchinterval(): 返回线程切换时间间隔, 默认0.005秒"] = "sys.getswitchinterval()"
    info["sys.setswitchinterval(interval): 设置线程切换的时间间隔, 单位秒"] = "sys.setswitchinterval(60)"
    info["sys.hash_info: 返回Python默认的哈希方法的参数"] = f"{sys.hash_info}"
    info["sys.implementation: 当前正在运行的Python解释器的具体实现, 比如CPython"] = f"{sys.implementation}"
    info["sys.thread_info: 当前线程信息"] = f"sys.thread_info = {sys.thread_info}"
    return info

def main():
    return {**self_attr_related(), **system_related(), **program_related()}
    
if __name__ == "__main__":
    import os, json
    
    info = main()
    
    curdir = os.path.split(__file__)[0]   # 本代码文件所在目录
    
    name = os.path.basename(os.path.splitext(__file__)[0])  # 本代码文件的无后缀文件名
    
    with open(f"{curdir}/{name}.json", "w") as f:
        f.write(json.dumps(info, 
                           indent=4,
                           ensure_ascii=False))

