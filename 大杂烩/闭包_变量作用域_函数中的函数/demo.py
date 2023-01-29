#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   demo.py
@Time    :   2022/12/10 18:19:41
'''
x = "global x"

def main():
    z = "outer z"
    
    def inner(y):
        return x, y, z
    
    return inner("y args")

print(main())

