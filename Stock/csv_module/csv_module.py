#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   csv_module.py
@Time    :   2022/11/27 10:43:05
'''
import os, csv


curdir = os.path.dirname(__file__)
file_path = os.path.join(curdir, "10年天气数据.csv")

assert os.path.exists(file_path) is True

def main():
    with open(file_path, "r", newline="", encoding="utf8") as csv_file:
        o = csv.reader(csv_file)
        for row in o:
            print(", ".join(row))



if __name__ == "__main__":
    main()
