#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   random_module.py
@Time    :   2022/11/19 21:35:45
'''
import random, string
random.choice(string.ascii_letters)

def main():
    info = {}
    
    # 随机一个数
    info["random.randint(): Random a float--between 0.0 and 1.0"] = random.randint()
    info["random.uniform(2.5, 10): Random a float--between 2.5 and 10)"] = random.uniform(2.5, 10)
    
    # 随机抽样
    random.choice([i for i in range(10)])
    random.choices(["red", "black"], [1, 4], k=3) # ["red", "black", "black", "black", "black"]
    random.sample(range(1000), k=60) # 简单随机抽样, 样本数量(返回的列表的长度)为k
    random.sample(["red", "black"], counts=[3, 1],k=60) # =["red", "red", "red","black"]
    
    # 搅匀/打乱/Shuffle(311中移除了)
    # l = [i for i in range(10)]
    # random.shuffle(l)
    return info
    


if __name__ == "__main__":
    # info = main()
    import json, os
    curdir = os.path.dirname(__file__)
    name = os.path.basename(__file__)
    stat = os.stat(__file__)
    print(curdir, name, stat, __name__, sep="\n")
    
