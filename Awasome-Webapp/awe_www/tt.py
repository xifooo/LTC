import weakref

# 定义一个类
class MyClass:
    pass

# 创建对象的弱引用
my_obj = MyClass()
my_ref = weakref.ref(my_obj)

# my_ref = weakref.ref(MyClass())

# 根据弱引用获取对象
obj = my_ref()

# 如果对象存在，打印对象的类型和地址
if obj:
    print(type(obj), id(obj))
else:
    print('Object has been garbage collected')
