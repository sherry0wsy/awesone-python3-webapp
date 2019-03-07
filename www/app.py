# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# author：wsy


import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

async def index(request):
    """
    处理URL，之后与具体URL绑定
    """
    return web.Response(body='<h1>Awesome</h1>'.encode(), content_type='text/html')

@asyncio.coroutine
def init(loop):
    # 创建Web服务器，并将处理函数注册进其应用路径
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    # 用协程创建监听服务，并使用aiohttp中的HTTP协议簇
    srv = yield from loop.create_server(app._make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop() # 获取EventLoop
loop.run_until_complete(init(loop)) # 执行coroutine
loop.run_forever()
