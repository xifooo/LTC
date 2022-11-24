#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   bt.py
@Time    :   2022/11/14 13:50:59
'''
import dataclasses


@dataclasses.dataclass(frozen=False)
class int_binary_tree():
    def __init__(self, i:int, left:"int_binary_tree", right:"int_binary_tree") -> None:
        self.i = i
        self.left = left
        self.right = right
        
    def sum_all(self):
        ans = self.i
        if self.left != None:
            ans = ans + self.left.sum_all()
        if self.right != None:
            ans = ans + self.right.sum_all()
        return ans
    @staticmethod
    def max_array():
        ...

def main():
    ...


if __name__ == "__main__":
    main()
