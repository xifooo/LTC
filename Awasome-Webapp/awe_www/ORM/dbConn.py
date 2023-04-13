#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import aiomysql, asyncio
from typing import Optional
from contextlib import asynccontextmanager

@asynccontextmanager
async def ConnectionPool():
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
    "loop": asyncio.get_running_loop()
    }
    pool = await aiomysql.create_pool(**dbConfig)
    try:
        yield pool
    finally:
        pool.close()
        await pool.wait_closed()

async def main():
    async with ConnectionPool() as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT * FROM Score;")
                result = await cur.fetchall()
                print(result)


# if __name__ == "__main__":
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(main())
#     loop.close()

