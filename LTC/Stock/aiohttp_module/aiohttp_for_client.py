#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   aiohttp_for_client.py
@Time    :   2022/11/18 14:28:22
'''
import aiohttp, asyncio, async_timeout, ujson


async def fetch(session, url):
    '''the begin of using aiohttp module'''
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            print (await f"{response.text()} \n {response.status}")

async def post(session, url):
    '''post method in the http protocol'''
    async with session.post(url["hb.post"], data=b'data') as resp:
        print(await f"{resp.text()} {resp.status}")

    
async def main():
    '''程序入口, 启动一个会话(session)'''
    url = {
        "hb.get": "http://httpbin.org/get",
        "hb.put": "http://httpbin.org/put",
        "hb.post": "http://httpbin.org/post",
        "hb.del": "http://httpbin.org/delelte",
        "hb.head": "http://httpbin.org/head",
        "hb.patch": "http://httpbin.org/patch",
        "hb.options": "http://httpbin.org/options",
        "pyorg": "http://python.org"
    }
    async with aiohttp.ClientSession() as session:
    # async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session: # 指定其它的json解析器
        html = await fetch(session, url)
        
        # session.post(url["hb.post"], data=b'data')
        # session.post(json={'test': 'object'}, data=b'data')  # 传递json
        # session.put('http://httpbin.org/put', data=b'data')
        # session.delete('http://httpbin.org/delete')
        # session.head('http://httpbin.org/get')
        # session.options('http://httpbin.org/get')
        # session.patch('http://httpbin.org/patch', data=b'data')
        print(html)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())