import inspect
import functools

def check(fn):
    
    @functools.wraps(fn)   # 等于 wrapper.__annotation__ = fn.__annotation__ 还有其他的属性比如__doc__，__module__等
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)   # 获取add函数签名信息
        params = sig.parameters     # 获取add函数的参数信息
        values = list(params.values())   # 由于params是个有序字典，那么values也是有序的，只需根据索一一对应判断即可
        for i, k in enumerate(args):   # 遍历用户传入的位置参数
            if values[i].annotation != inspect._empty:   # 如果定义了参数注解，则开始检查
                if not isinstance(k, values[i].annotation):   # 如果检查不通过，曝出异常
                    raise('Key Error')
        for k,v in kwargs.items():
            if params[k].annotation != inspect._empty:
                if not isinstance(v,params[k].annotation):
                    raise('Key Error')
        print(sig, params, values)
        return fn(*args, **kwargs)
    
    return wrapper

@check
def add(x: int, y: int) -> int:
    return x + y
    
print(add(4,y=5))