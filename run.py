# -*- coding: utf-8 -*-
# coding=utf-8


from flask import Flask
from flask import request
from leecher import search4zimu
import json
import leancloud
leancloud.init("gKyFTeBG9xK1fgUhXqwFyacL-gzGzoHsz", "YwxyNi07J0NT9DhH3QdRK4LD")
leancloud.use_region('CN') # 默认启用中国节点
ZimuObject = leancloud.Object.extend('Zimu')
zimu = ZimuObject()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/search')
def search():
    keyword = request.args.get('keyword', '')
    result = search4zimu(keyword.encode('utf-8'))
    urls = []
    names = []
    for k,v in result.items():
        print k,v
        urls.append(k)
        names.append(v)
    zimu.set('url',urls[0])
    zimu.set('name',names[0])
    zimu.save()
    return urls[0]
if __name__ == '__main__':
    app.run()