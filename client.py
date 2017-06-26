# encoding:utf-8
import urllib.request


def main():
    print('==== Test1 start ====')
    talk_with_remote_host(hostname='cn.bing.com', port=80)
    print('==== Test1 end ====')

    print('==== Test2 start =====')
    obj = urllib.request.urlopen('http://cn.bing.com/')
    data = obj.read()
    print(data)
    file = open("index.html", mode='wb')
    file.write(data)
    file.close()
    print('==== Test2 end ====')


from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from socket import SHUT_RDWR


def talk_with_remote_host(hostname, port):
    """手动创建 Socket 进行 TCP 通讯测试
    :type hostname: str
    :type port: int
    """
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((hostname, port))
    item = '/'
    http_request = \
        'GET {} HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n'.format(item, hostname)
    # 发送 HTTP 请求
    s.send(bytes(http_request, 'utf-8'))

    # 接收数据:
    buf_list = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if not d:
            s.shutdown(SHUT_RDWR)  # 停止数据读写
            break
        buf_list.append(d)
    with open("HTTP_RESPONSE.log", mode='wb') as file:
        for i in buf_list:
            file.write(i)
    s.close()
    return


if '__main__' == __name__:
    main()
