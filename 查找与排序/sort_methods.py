#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random


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

def quick_sort(lst, low, high):
    """Quick sort"""
    if low >= high:
        return
    cur_ele = lst[low]
    
    left, right = low, high
    
    while low < high:
        # 处理右边
        while (low < high) and (lst[high] >= cur_ele):
            high -= 1
        lst[low] = lst[high]
        # 处理左边
        while (low < high) and (lst[low] <= cur_ele):
            low += 1
        lst[high] = lst[low]
    # low=high时完成一次全处理/划分
    lst[high] = cur_ele
    # 对两边分别进行全处理/划分
    quick_sort(lst, left, low - 1)
    quick_sort(lst, low + 1 , right)

def insert_sort(seq):
    """排序: 插入排序"""
    
    for i in range(1, len(seq)):
        cur_ele = seq[i]
        j = i-1
        
        while cur_ele > seq[j] and j >= 0:
            seq[j+1] = seq[j]
            j = j-1
        seq[j+1] = cur_ele

def insert_sort_pro(seq):
    """插入排序的优化 = 插入排序 + 二分查找"""
    for i in range(1, len(seq)):
        cur_ele = seq[i]
        ...
    ...

def bubble_sort(seq):
    """排序: 冒泡排序"""
    seq = list(seq)
    print(f"排序前: {seq}")
    for i in range(len(seq)):
        for j in range(len(seq)-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    # flag = True
    # while flag:
    #     flag = False
    #     for i in range(len(seq)-1):
    #         if seq[i] > seq[i + 1]:
    #             flag = True
    #             seq[i], seq[i + 1] = seq[i + 1], seq[i]
    print(f"排序后: {seq}")
    return

def selection_sort(seq):
    """排序: 选择排序"""
    seq = list(seq)
    print(f"排序前: {seq}")
    for i in range(len(seq)):
        ith = i
        for j in range(i+1, len(seq)):
            if seq[j] <= seq[ith]:
                ith = j
        seq[i], seq[ith] = seq[ith], seq[i]
    print(f"排序后: {seq}")
    return


def main():
    ...


if __name__ == "__main__":
    main()
