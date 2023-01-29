#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   views.py
@Time    :   2022/11/19 17:17:52
'''
from aiohttp import web


async def index(request):
    return web.Response(text="Hellow aiohttp!")


