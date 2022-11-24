#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   main.py
@Time    :   2022/11/19 17:16:33
'''
from aiohttp import web
from routes import setup_routes


if __name__ == "__main__":
    app = web.Application()
    setup_routes(app)
    web.run_app(app,
                host = "127.0.0.1",
                port = 1888)
