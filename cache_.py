import random,inspect, functools

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

def checque(func):
    
    @functools.wraps(func)
    def inner(*args, **kwargs):
        seq = list(disorder_lst_gen(15))
        print(f"排序前: {seq}")
        func(seq, *args, **kwargs)
        print(f"排序后: {seq}")
        return 
        
    return inner


@checque
def _sort(seq):
    print(seq, "_sort")
    return 0

_sort()
