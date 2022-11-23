#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   use_os_module.py
@Time    :   2022/11/11 10:12:42
uncompleted
'''
import os, re, json, logging


def get_computer_info():
    info = {}
    
    # 硬件信息
    info["NUMBER_OF_PROCESSORS: CPU数量"] = os.environ["NUMBER_OF_PROCESSORS"]
    info["PROCESSOR_ARCHITECTURE: CPU架构"] = os.environ["PROCESSOR_ARCHITECTURE"]
    info["PROCESSOR_IDENTIFIER: CPU标识符"] = os.environ["PROCESSOR_IDENTIFIER"]
    info["PROCESSOR_LEVEL: CPU级别"] = os.environ["PROCESSOR_LEVEL"]
    
    # 操作系统
    info["OS: 操作系统"] = os.environ["OS"]

    # 用户信息
    info["USERNAME: 用户名"] = os.environ["USERNAME"]
    
    # d = os.environ["PATH"]
    # pattern = re.compile(r"C:\\Users\\\w*")
    # # 用户变量的PATH
    # pattern.match(d)
    # # 系统变量的PATH
    return json.dumps(info, indent=4, ensure_ascii=False)

def main():
    try:
        print(json.loads(get_computer_info()))
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":
    main()
