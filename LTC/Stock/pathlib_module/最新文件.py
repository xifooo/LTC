#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   最新文件.py
@Time    :   2022/11/26 09:51:53
'''
def main():
    from pathlib import Path
    folder_path = Path(__file__).parent
    list_of_files = folder_path.glob("*")
    latest_path = max(list_of_files, key=lambda p: p.stat().st_ctime)
    print(latest_path)


def sec_main():
    import glob, os
    curdir = os.path.dirname(__file__)
    list_of_files = glob.glob(f"{curdir}/*")
    latest_file = max(list_of_files, key= os.path.getctime)
    print(latest_file)
    
if __name__ == "__main__":
    main()
    sec_main()
