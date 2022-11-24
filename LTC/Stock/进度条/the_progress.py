#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   progress_module.py
@Time    :   2022/11/23 21:22:18
'''
from progress.bar import Bar

def main():
    bar = Bar("Progressing", max = 20)
    for i in range(20):
        # do something
        bar.next()
    bar.finish()

if __name__ == "__main__":
    main()
