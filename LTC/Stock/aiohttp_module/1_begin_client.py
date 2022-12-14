#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   1_begin.py
@Time    :   2022/11/18 14:36:37
'''
import aiohttp, asyncio, async_timeout

async def fetch(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()
    
async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "http://python.org")
        print(html)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
