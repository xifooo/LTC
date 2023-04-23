+ 第一部分：协程

+ 第二部分：asyncio模块

+ 第三部分：实战

## 协程

+ “微线程”，人为控制。多进程、多线程由OS控制。

+ 实现协程（python）  
    greenlet，早期模块（后面还有gevent）  
    yield关键字  
    asyncio装饰器（py3.4）  
    async、await关键字（py3.5）

## 事件循环 Event Loop

+ 所有的协程任务都使用同一个循环队列。asyncio的核心：一个event loop。

    ```python

    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Coroutine Function / Task)

    ```

## 协程函数 Coroutine Function & 协程对象 Coroutine Object

+ 就同于python的 generator，call 一个 coroutine function得到一个 coroutine object.

```python

...

result = func()
loop = asyncio.get_event_loop()
loop.run_until_complete(result)

# 或者

loop = asyncio.get_event_loop()

loop.run_until_complete(func())

# py3.7以后，这两个都可

asyncio.fun(result)

asyncio.run(func())

```

## await

await + awaitable Object (Coroutine Object / Coroutine Function call、Future、Task Object)

## Task Object

+ 官方定义：Task对象是Future的一个子类，它代表正在进行的协程，具有一个coroutine属性，该属性引用正在执行的协程。Task对象由事件循环调度和运行。

+ 理解：Task对象是一个可等待对象，代表协程的执行。它可以被用来暂停和恢复协程的执行，也可以被用来管理协程的状态，如取消、重置等。

```python

...

# 将一个 Coroutine Object 包装成一个 Task，并立即加入到Event Loop中去。

# py3.7之前

asyncio.ensure_future(f1())

# py3.7及以后

asyncio.create_task(f2())



# py3.8以后，给Task命名

asyncio.create_task(f3(), name="f3 call")

```

```python

task_list = [

    f1(), f2(), f3()

]

# await asyncio.wait()批量等待task_list里的Coroutine Objects完成

await asyncio.wait(task_list)

# done是一个集合，包含已经完成的任务（即已经成功完成或者抛出异常），pending是一个集合，包含还未完成的任务。timeout=2表示最多等待2s，也可设为None。通过done集合中的result()方法获取已完成任务的结果。

done, pending = await asyncio.wait(task_list, timeout=2)



# 省代码写法

done, pending = asyncio.run( asyncio.wait( task_list) )

```

## future1

+ 官方定义：Future表示异步计算的结果，它提供了一个等待长时间运行的计算完成而不阻塞程序主执行线程的方法。简单来说，Future是用来处理异步操作结果的一种机制。

+ Future是一种特殊的对象，它表示一个尚未完成的操作的结果。

++ 单纯的一个Future object 永远不会主动结束，

## Future2

+ concurrent.futures.Future

使用线程池、进程池实现异步操作时用到的对象

```python

from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor

import time

def func(v):
   time.sleep(1)
   print(v)
# 创建线程池
pool = ThreadPoolExecutor(max_workers=5)

# 创建进程池
# pool = ProcessPoolExecutor(max_workers=5)

for i in range(10):
    # 所有任务几乎瞬间完成，之后把return值赋给fut
   fut = pool.submit(func, i)
   print(fut)

```



```python

import time, asyncio, concurrent.futures

def f1():
  time.sleep(1)
  return "go"

async def main():
  loop = asyncio.get_running_loop()

#   1.asyncio.wrap_future 将 concurrent.futures.Future对象转换成asyncio.Future对象
#   fut = loop.run_in_executor(None, f1)
#   result = await fut
#   print("default thread pool", result)

#   2. 用线程池
#   with concurrent.futures.ThreadPoolExecutor() as pool:
#     result = await loop.run_in_executor(pool, f1)
#     print("custom thread pool", result)

#   3. 用进程池
  with concurrent.futures.ProcessPoolExecutor() as pool:
    result = await loop.run_in_executor(pool, f1)
    print("custom process pool", result)

   
asyncio.run(main())


```


+ 小结：

    + python的协程的核心是一个循环队列event loop，在里面运行的作业对象都是Coroutine Object、都具有awaitable属性。

    + Coroutine Object指的是1.CoroutineFunctionCall; 2.Task; 3.Future

## 案例：asyncio+不支持异步的模块

## 异步迭代器

+ 有__aiter__和async __anext__方法的对象

```python

import asyncio

class Reader:
  def __init__(self):
    self.count = 0

  def readline(self):
    self.count += 1
    if self.count == 100:
      return None
    return self.count

  def __aiter__(self):
    return self

  async def __anext__(self):
    val = await self.readline
    if val is None:
      raise StopAsyncIteration
    return val

async def main():
    o = Reader()
    asynn for i in o:
        print(i)

asyncio.run(main())

```

## 异步上下文管理器

+ 有async __aenter__和async __aexit__方法的对象

```python

import asyncio

class ACM:

  def __init__(self):
    self.conn = None

  async def __aenter__(self):
    print("enter")

  async def __aexit__(self, exc_type, exc, tb):
    print("exit")   

async def main():
  o = ACM()
  async with o as o:
    print("ok")

asyncio.run(main())

```



## uvloop

+ asyncio默认的event loop的替代方案。（比肩go？）

```python

import asyncio, uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy)

...

```

+ 注意：一个知名的asgi ： uvicorn

++ ASGI一个Python的异步Web框架，Uvicorn是ASGI的一种实现，它是用Python编写的一个轻量级的高性能Web服务器。在简单的说法中，ASGI是为异步Web开发提供标准的接口协议，而Uvicorn是这个协议的一种实现。区别在于ASGI是一种接口协议，而Uvicorn是一个使用这个协议的Web服务器。



## 案例：异步操作Redis

+ 需要aioredis：pip install aioredis

```python

import asyncio, aioredis

async def execute(address, password):
  print("开始执行", address)

  # 网络IO操作：操作Redis连接
  redis = await aioredis.create_redis(address, password = password)

  # 网络IO操作：在redis中设置哈希值
  await redis.hmset_dict("car", key1=1, key2=2, key3=3)

  # 网络IO操作：在redis中获取值
  result = await redis.hgetall("car", encoding="utf-8")

  print(result)

  # 网络IO操作：关闭redis连接
  await redis.wait_closed()

  print("结束", address)

asyncio.run( execute("redis://127.0.0.1:7890", "root123123") )

```

## 案例：异步操作MySQL

+ 略

## 案例：FastAPI异步框架

+ 安装依赖：

    + pip install fastapi

    + pip install uvicorn #(asgi内部基于uvloop)

+ 一个简陋的web应用程序

```python

# main.py

import asyncio

import uvicorn

from fastapi import FASTAPI

app = FASTAPI()

@app.get("/")

def index():

    return {"message": "hello world"}

if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")

```

```python

# myApp.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_root():

  return {"Hello": "World"}



@app.get("/items/{item_id}")

def read_item(item_id: int, q: str = None):

  return {"item_id": item_id, "q": q}





uvicorn myApp:app --host 0.0.0.0 --port 5000

```