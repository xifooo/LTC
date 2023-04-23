__caution__ = """
这段代码存在以下两个问题：

单例模式不适用于异步环境。因为在多线程中出现竞争条件时，可能会导致实例化多次。更好的方法是使用asyncio中的@singleton装饰器。

ConnectionPool类应该继承AbstractAsyncContextManager类，以确保该类可以作为上下文管理器使用，从而可以使用async with语句自动管理资源。
"""

import threading
import aiomysql, asyncio
from typing import Optional

class ConnectionPool:
    _instance_lock = threading.Lock()

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super().__new__(cls)
                    cls._instance.pool = None
                    cls._instance.loop = asyncio.get_running_loop()
        return cls._instance

    async def get_connection(self) -> Optional[aiomysql.Connection]:
        if not self.pool:
            await self.create_pool()
        return await self.pool.acquire()

    async def create_pool(self):
        dbConfig = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "jyeeho",
            "password": "123321",
            "db": "50q",
            "charset": "utf8mb4",
            "autocommit": True,
            "maxsize": 10,
            "minsize": 1,
            "loop": self.loop
        }
        self.pool = await aiomysql.create_pool(**dbConfig)

    async def close_pool(self):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()
            self.pool = None

    async def __aenter__(self):
        self.conn = await self.get_connection()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.conn and self.loop:
            for conn in self.pool._used:
                conn.close()
                # await conn.wait_closed()
            # await self.pool.release(self)
            self.pool.close()
            await self.pool.wait_closed()
            self.conn = None

    async def shutdown(self):
        await self.close_pool()
        self.loop.stop()
        self.loop.close()
        
# dbConfig = {
#     "host": "127.0.0.1",
#     "port": 3306,
#     "user": "jyeeho",
#     "password": "123321",
#     "db": "50q",
#     "charset": "utf8mb4"
# }
'''
cls._instance.loop和self.loop一样吗

是的，cls._instance.loop 和 self.loop 指向的是同一个事件循环对象，
即 asyncio 模块中的事件循环。因为 cls._instance 是类（静态）属性，而 self 是实例属性。
但是，在 __new__() 方法中，由于使用了 Singleton 模式，cls._instance 始终指向唯一的实例对象，
所以 cls._instance.loop 和 self.loop 实际上是相同的事件循环对象。
因此，在 create_pool() 方法中调用的 aiomysql.create_pool() 方法将使用 cls._instance.loop 来创建和管理事件循环的所有任务。
'''
# connection_pool = ConnectionPool()

# async def main():

#     async with connection_pool as conn:
#         async with conn.cursor() as cur:
#             await cur.execute("select * from Score;")
#             result = await cur.fetchall()
#             print(result)
#     return
            
            
# if __name__ == "__main__":
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     connection_pool.loop = loop
#     loop.run_until_complete(main())
#     loop.close()