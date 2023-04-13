#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random


def disorder_lst_gen(lst_length:int):
    """
    disorder_lst_gen 生成指定长度的无序列表

    Args:
        lst_length (int): 长度

    Raises:
        TypeError: 非 int 类型
        ValueError: 负数
        ValueError: 长度太小了

    Returns:
        iterator: 一个无序序列的 generator
    """
    if not isinstance(lst_length, int):
        raise TypeError("the type of lst_length's value wrong ")
    if lst_length <= 0:
        raise ValueError("the list length could't be negative!")
    if 0 < lst_length <= 3:
        raise ValueError("the list length is too short!")
    
    seed = random.randint(2,5)
    return (i for i in random.sample(range(lst_length*seed), k=lst_length)*random.randint(2,5))

# def check_params(func):
#     '检查入参的类型、'
#     def inner(*args, **kwargs):
#         if not isinstance()
#         for arg in args:
#         return
#     return inner
# from contextlib import contextmanager


# @contextmanager
# def disorder_lst_pool(lst_length:int):
#     """ 
#     Return a disordered sequence whose length equal to lst_length
#     """
#     if not isinstance(lst_length, int):
#         raise TypeError("the type of lst_length's value wrong ")
    
#     if lst_length <= 0:
#         raise ValueError("the list length could't be negative!")
#     if 0 < lst_length <= 3:
#         raise ValueError("the list length is too short!")
    
#     yield [i for i in random.sample(range(100), k=lst_length)]