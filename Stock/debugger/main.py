def g(data):
    return data * data

def f(x):
    breakpoint()
    lst = []
    for _ in range(10):
        val = g(_)
        lst.append(val)
    return lst

f(3)