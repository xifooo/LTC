#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   json_module.py
@Time    :   2022/11/08 22:18:39
'''
import json, os

about_json = """
在Python中json是全部小写的, 包括模块和方法名;
Json是跨语言, 跨平台的, 但只能对Python的基本数据类型做操作, 对Python的类就无能为力;
json的数据要求用双引号将字符串引起来, 并且不能有多余的逗号.
load到python中,dump到json, 根据字符串转化就加's', 要从文件进行转化就不加's'.
"""

def collation():
    py_to_json = {
        "Python": "Json",
        "dict": "object",
        "list, tuple": "array",
        "str": "string",
        "int, float, int- & float-derived Enums": "number",
        "True": "true",
        "False": "false",
        "None": "null"
         }
    json_to_py = {
        "Json": "Python",
        "object": "dict",
        "array": "list",
        "string": "str",
        "number(int)": "int",
        "number(real)": "float",
        "true": "True",
        "false": "False",
        "null": "None"
    }
    return (json_to_py, py_to_json)


def main():
    info = {}
    info["json_to_py"], info["py_to_json"] = collation()
    curdir = os.path.dirname(__file__)
    with open(f"{curdir}/json_module.json","w") as f:
        f.write(json.dumps(info, 
                           indent = 4,
                           ensure_ascii = False,  # False-字符会原样输出, True-将所有输入的非 ASCII 字符转义
                           # encoding = "utf-8",  # py3.9已经移除了
                           skipkeys = False,  # False-非基本对象的字典的键将不会被跳过, 若存在非基本对象的key,则抛出TypeError
                           ))
        f.write("\n")

if __name__ == "__main__":
    main()

