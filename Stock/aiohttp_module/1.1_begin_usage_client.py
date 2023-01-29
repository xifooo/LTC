#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   1.1_begin_usage_client.py
@Time    :   2022/11/18 14:54:27
'''
import aiohttp, asyncio, logging 


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.github.com/events") as resp:
            print(resp.status)
            print(await resp.text())


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        # 对未使用SSL的ClientSession
        # loop.run_until_complete(asyncio.sleep(0))
        # 对使用SSL的ClientSession
        loop.run_until_complete(asyncio.sleep(0.250))
    except ResourceWarning as e:
        logging.warning(e)
    finally:
        loop.close()
