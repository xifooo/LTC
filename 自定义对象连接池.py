from contextlib import contextmanager
import random
# https://zhuanlan.zhihu.com/p/73355377

"""
尝试实现一个类似数据库连接池的object
"""
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
    
with disorder_lst_pool(lst_length=10) as lst:
    print(lst)