"查找列表中最大的一个数"
import timeit


lst = [2,3,4,6,1,99,29,5,48,10]
the_largest_one = int(sum([i ** 100 for i in lst]) ** (1/100))
print(the_largest_one)

setup = """
"""

test_code_1 = """
lst = [2,3,4,6,1,99,29,5,48,10]
the_largest_one = int(sum([i ** 100 for i in lst]) ** (1/100))
"""
test_code_2 = """
lst = [2,3,4,6,1,99,29,5,48,10]
the_largest_one = max(lst)
"""

taking_time_1 = timeit.timeit(stmt=test_code_1, setup=setup,number=10_000)
taking_time_2 = timeit.timeit(stmt=test_code_2, setup=setup,number=10_000)

print(taking_time_1)
print(taking_time_2)

# 但是还是比max()慢
