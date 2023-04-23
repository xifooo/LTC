#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import math
from functools import reduce
from utils import disorder_lst_gen

def quick_sort(A:list, low:int, high:int):
    """
    quick_sort 排序: 快排, 直接对目标 list object排序

    Args:
        A (list): 待排序list
        low (int): 最低位的index
        high (int): 最高位的index
    """
    if low >= high:
        return
    cur_ele = A[low]

    left, right = low, high

    while low < high:
        # 处理右边
        while (low < high) and (A[high] >= cur_ele):
            high -= 1
        A[low] = A[high]
        # 处理左边
        while (low < high) and (A[low] <= cur_ele):
            low += 1
        A[high] = A[low]
    # low=high时完成一次全处理/划分
    A[high] = cur_ele
    # 对两边分别进行全处理/划分
    quick_sort(A, left, low - 1)
    quick_sort(A, low + 1 , right)


def insert_sort(A:list):
    """
    insert_sort 排序: 插入排序

    Args:
        A (_type_): _description_
    """
    for i in range(1, len(A)):
        cur_ele = A[i]
        j = i-1
        
        while cur_ele > A[j] and j >= 0:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = cur_ele


def insert_sort_pro(seq:list):
    """插入排序的优化 = 插入排序 + 二分查找"""
    for i in range(1, len(seq)):
        cur_ele = seq[i]
        ...
    ...

def bubble_sort(seq:list):
    """
    bubble_sort 排序: 冒泡排序

    Args:
        seq (_type_): _description_
    """
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


def selection_sort(seq:list):
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

def selection_sort_recur(seq:list):
    """
    selection_sort_recur 选择排序的递归版

    Args:
        seq (list): 待排序 list
    """
    def prefix_max(A, i):
        """
        prefix_max return the maxium of A[:i-1]
        """
        if i > 0:
            j = prefix_max(A, i - 1)
            if A[i] < A[j]:
                return j
        return i

    def _sort(A, i = None):
        if i is None: i = len(A) - 1
        if i > 0:
            j = prefix_max(A, i)
            A[i], A[j] = A[j], A[i]
            _sort(A, i-1)
            
    _sort(seq, i=len(seq)-1)
    
# 你的代码使用了Python的递归方法实现了归并排序。这种方法将待排序列表不断地切割成更小的列表，然后逐步将它们合并回一个已排序的列表。

# 在merge()函数中，我们首先检查左列表L和右列表R。如果它们都非空，我们将两个列表中最后一个元素中比较小的那个放到已排序的列表A的末尾。然后我们将A的索引指向刚刚添加的那个元素，再对短的那个列表调用递归自己。

# 在merge_sort()函数中，我们首先检查待排序序列A的长度。如果长度小于等于1，则返回原始序列。否则，我们计算A的中点，然后分别递归地调用左半边和右半边，接着将左半边和右半边分别传递给merge()函数进行合并。

# 虽然这个方法更易于理解和阅读，但它的空间复杂度比迭代方法高，因为它需要创建多个函数调用堆栈来保存中间结果。在Python中，由于递归深度的限制，这可能导致执行失败。所以，更常用的是迭代法归并排序。
def merge_sort(A:list):
    """
    merge_sort_ 归并排序

    Args:
        A (list): 待排序序列
    """
    
    def merge(L:list, R:list, A:list, i:int, j:int, a:int, b:int):
        """
        merge 合并两个有序序列

        Args:
            L (list): 第一个待排序的有序序列L
            R (list): 第二个待排序的有序序列R
            A (list): 原始的待排序序列A
            i (int): len(L)
            j (int): len(R)
            a (int): _description_
            b (int): _description_
        """
        if a < b:
            if (j <= 0) | (i > 0 and L[i-1] > R[j-1]):
                A[b-1] = L[i-1]
                i = i-1
            else:
                A[b-1] = R[j-1]
                j = j-1
            merge(L, R, A, i, j, a, b-1)

    def merge_sorting(A:list, a=0, b=None):
        """
        merge_sort Sort A[a:b]

        Args:
            A (list): 待排序数组
            a (int, optional): 所有待排序元素的起点位置. Defaults to 0.
            b (_type_, optional): 所有待排序元素的结束位置. Defaults to None.
        """
        if b is None: b = len(A)
        if 1 < b - a:
            c = (a+b+1) // 2
            merge_sorting(A, a, c)
            merge_sorting(A, c, b)
            L, R = A[a:c], A[c:b]
            merge(L, R, A, len(L), len(R), a, b)
    merge_sorting(A)
    return A

def count_sort(A:list):
    """
    count_sort 计数排序, 稳定的线性时间的排序算法。 总体有序, 局部的相对顺序不变

    Args:
        A (list): 待排序序列
    """
    length = math.ceil(math.log(len(A), 2))
    # Direct Access Array: 二维数组
    DAA = [[] for _ in range(length)]
    
    for item in A:
        DAA[item // length].append(item)

    A = [ x for y in DAA for x in y]

def radix_sort(A:list):
    # 可进行字符串排序
    # m = get_max(A)
    ...
    

def main():
    A = list(disorder_lst_gen(100))
    
    print(f"排序前：{A}")
    
    # quick_sort(A, 0, len(A)-1)
    # insert_sort(A)
    # bubble_sort(A)
    # selection_sort(A)
    # selection_sort_recur(A)
    merge_sort(A)
    # count_sort(A)
    
    print(f"排序后：{A}")


if __name__ == "__main__":
    main()
    
    # import timeit
    # elapsed_time = timeit.timeit(main, number=100)
    # print("执行时间：", elapsed_time, "秒")
