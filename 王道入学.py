from functools import wraps,reduce
import random
import math

def sep_sign(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    print("--sep--".center(50, "-"))
    return inner

@sep_sign
def question_7():
    """7, 随机数生成，[0,100]内的10个"""
    print( f"{question_7.__doc__}\n{random.sample(range(101),k=10)}" )
question_7()

@sep_sign
def question_8():
    """8, 打印倒三角形"""
    print(question_8.__doc__)
    for i in reversed(range(4)):
        print("*" * (i+1) )
    return
question_8()

@sep_sign
def question_14(**kw):
    """14, 读取两个数a和b, 输出a和b中较大的"""
    print(question_14.__doc__)
    # a和b的差的绝对值是否小于一个比较小的值
    if math.fabs(kw["a"]-kw["b"]) < 0.000_000_000_001:
        print("two numbers is equal")
    elif kw["a"] > kw["b"]:
        print(f"{kw['a']} greater than {kw['b']}")
    elif kw["b"] > kw["a"]:
        print(f"{kw['b']} greater than {kw['a']}")
    return

# a, b = input("Get the bigger of two numbers(seperated by a Dot):").split(",")
# question_14(eval(a), eval(b))
question_14(**dict( zip(
        ["a","b"],
        [eval(i) for i in input("Get the bigger of two numbers(seperated by a Dot):").split(",")]
        )
    ))

@sep_sign
def question_15(a,/):
    """15, 判断质数"""
    if a < 2 or isinstance(a, float):
        print(f"{a} 不是质数")
        return
    # 02357
    if a == 2:
        print(f"{a} 是质数")
        return
    elif a % 2 == 0 or a % 5 == 0 or a % 3 == 0:
        print(f"{a} 不是质数")
        return
    elif a % 7 == 0:
        print(f"{a} 不是质数")
        return
    else:
        print(f"{a} 是质数")
        return
question_15(eval(input("判断是否为质数:")))

@sep_sign
def question_16():
    """16, 输出[0,100]（左闭右闭区间）内的素数"""
    print(question_16.__doc__)
    lst = []
    for item in range(2, 101):
        if item % 2 == 0 or item % 3 == 0 or item % 5 == 0:
            pass
        elif item % 7 == 0:
            pass
        else:
            lst.append(item)
    print(lst)
    return

question_16()

@sep_sign
def question_17(a:int):
    """17, 阶乘"""
    ret = reduce(lambda x,y: x*y, range(1,a+1))
    print(f"{a}! = {ret}")
    return
question_17(int(input("计算阶乘：")))

@sep_sign
def question_19(a:int):
    """19, 1到输入数字之间的斐波那契数列"""
    fibo = [1, 2]
    # [fibo.append(fibo[-2]+fibo[-1]) for i in range(a-2)]
    [fibo.append(fibo[-2]+fibo[-1]) for i in range(a-2) if fibo[-2]+fibo[-1]<=a]
    # for _ in range(a-2):
    #     if fibo[-2] + fibo[-1] > a:
    #         break
    #     fibo.append(fibo[-2] + fibo[-1])
    print(fibo)
    return 

question_19(eval(input("生成 n+1 个斐波那契数:")))