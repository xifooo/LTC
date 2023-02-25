#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random
import typing
from contextlib import contextmanager


@contextmanager
def disorder_lst_pool(lst_length:int):
    """ 
    Return a disordered sequence whose length equal to lst_length
    """
    if not isinstance(lst_length, int):
        raise TypeError("the type of lst_length's value wrong ")
    
    if lst_length <= 0:
        raise ValueError("the list length could't be negative!")
    if 0 < lst_length <= 3:
        raise ValueError("the list length is too short!")
    
    yield [i for i in random.sample(range(100), k=lst_length)]


def disorder_lst_gen(lst_length:int):
    """ 
    Return a disordered sequence whose length equal to lst_length
    """
    if not isinstance(lst_length, int):
        raise TypeError("the type of lst_length's value wrong ")
    
    if lst_length <= 0:
        raise ValueError("the list length could't be negative!")
    if 0 < lst_length <= 3:
        raise ValueError("the list length is too short!")
    
    return (i for i in random.sample(range(100), k=lst_length))


def order_lst_gen(lst_length:int):
    """
    Return a ordered sequence (increasing from left to right) whose length equal to lst_length
    """
    if not isinstance(lst_length, int):
        raise TypeError("the type of lst_length's value wrong ")
    
    if lst_length <= 0:
        raise ValueError("the list length could't be negative!")
    if 0 < lst_length <= 3:
        raise ValueError("the list length is too short!")
    # quick sort
    def quick_sort(lst, low, high):
        """directly sort a list self"""
        if low >= high:
            return
        cur_ele = lst(low)
        left, right = low, high
        while low < high:
            while (low < high) and (lst[high] >= cur_ele):
                high -= 1
            lst[low] = lst[high]
            while (low < high) and (lst[low] <= cur_ele):
                low += 1
            lst[high] = lst[low]
        lst[high] = cur_ele
        quick_sort(lst, left, low-1)
        quick_sort(lst, low+1, right)
    L = [i for i in random.sample(range(100), k=lst_length)]
    quick_sort(L, 0, len(L)-1)
    print(L)
    return L


def find_maximum(seq, *args):
    """闵可夫斯基距离法"""
    if (not isinstance(seq, typing.Generator)) and (not isinstance(seq, list)):
        raise TypeError("Type of the input list come wrong!")
    
    maximum = int(sum([item ** 100 for item in seq]) ** (1/100))
    print("The maximum value is ",maximum, sep="\n")
    return maximum


def find_minimum(seq, *args):
    """Print the minimum of list and Return it"""
    if (not isinstance(seq, typing.Generator)) and (not isinstance(seq, list)):
        raise TypeError("Type of the input list come wrong!")
    ...
    
    
def binary_search(seq):
    """二分法"""
    ...
    
if __name__ == "__main__":
    try:
        length = int(input("Please type your expected a list length: "))
        
        disordered_lst = disorder_lst_gen(length)

        find_maximum(disordered_lst)
        # 如何建立一个随机数序列生成池
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
