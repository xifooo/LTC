#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   larges-for-lon.py
@Time    :   2022/11/15 10:29:54
origin:
(define (largest-for-lon lon)
  (cond [(empty? lon) 0]
        [else
         (if (> (first lon) (largest-for-lon (rest lon)))
             (first lon)
             (largest-for-lon (rest lon)))]))
'''
from collections import deque

def rest_lon(lon:deque):
    return 

def largest(lon:deque):
    if not lon:
        return 0
    else:
        if lon[0] > largest(rest_lon(lon)):
            return lon[0]
        else:
            largest(rest_lon(lon))


def main():
    lst = [2,3,4,6,1,99,29,5,48,10]
    lon = deque(lst)
    


if __name__ == "__main__":
    main()
