#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from ORM import dbConn
import asyncio, uvloop

async def main():
    async with dbConn.ConnectionPool() as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("select * from Score;")
                result = await cur.fetchall()
                print(result)



if __name__ == "__main__":
    # # loop = asyncio.new_event_loop()
    # # asyncio.set_event_loop(loop)
    # # dbConn.connection_pool.loop = loop
    # # loop.run_until_complete(main())
    # # loop.close()
    
    
    # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy)
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()
    
