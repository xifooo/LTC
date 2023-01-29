#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   routes.py
@Time    :   2022/11/19 17:19:12
'''
from views import index


def setup_routes(app):
    app.router.add_get("/", index)


