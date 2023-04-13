#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# import logging
# import asyncio
from aiohttp import web

async def index(req):
    return web.Response(body=b'<h1>Awesome Website</h1>', content_type='text/html')

def main():
    app = web.Application()
    router = app.router
    
    router.add_get("/", index)
    web.run_app(
        app,
        host="127.0.0.1",
        port=9000
    )

def main2():
    app = web.Application()
    router = app.router
    
    routers = web.RouteTableDef()
    
    router.add_routes(routers)
    router.add_prefix("/api")
    
    app.router.add_subapp("/api", routers)
    
    web.run_app(
        app,
        host="127.0.0.1",
        port=9000
    )

if __name__ == "__main__":
    main()
