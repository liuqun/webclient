#!/usr/bin/env python3
# encoding: utf-8
from urllib.request import urlopen
from urllib.request import URLError


if '__main__' == __name__:
    print('==== TEST START ====')
    url = 'http://cn.bing.com/'
    response = None
    try:
        response = urlopen(url)
        if response.status >= 300:
            print('STATUS: ', response.status, '(', response.reason, ')')
        data = response.read()
        print('data=', data)  # 取回的数据默认以二进制形式存储, 其中的汉字编码可能是 UTF-8 或 GB2312
        with open("index.html", mode='wb') as file:
            file.write(data)
    except URLError as e:
        print('An error happened while trying to visit', url, '. Error message:',e)
    print('==== TEST END ====')
