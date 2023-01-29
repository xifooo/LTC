#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   1_begin_server.py
@Time    :   2022/11/18 14:43:44
'''
from aiohttp import web


async def handle(request):
    name = request.match_info.get("name", "Anonymous")
    text = f"Hello {name}"
    return web.Response(text=text)


if __name__ == "__main__":
    app = web.Application()
    app.router.add_get("/", handle)
    app.router.add_get("/{name}", handle)
    web.run_app(app=app)
