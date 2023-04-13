#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aiohttp.web import RouteTableDef

router = RouteTableDef()

@router.get("/")
async def index(req, res):
    ...