from bottle import route, run,request


@route('/hello', method='post')
def hello():
    for key,value in request.params.items():
        print(key,value)

    request.url
    request.method
    request.headers
    request.body

    import urllib3,json
    http = urllib3.PoolManager()  # 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
    response = http.request(request.method, 'http://localhost:8082/hello', headers=request.headers,body=request.json)  # get方式请求
    print(response.status, response.data.decode('utf-8'))  # 获得状态码, html源码(utf-8解码)

    # import urllib3
    # proxy = urllib3.ProxyManager('http://10.10.28.13:10701')
    # proxy.request('GET', 'http://google.com/')

    print(request.params)
    return "Hello World!"

if __name__ =="__main__":
    run(host='localhost', port=8083, debug=True)


    def mea_mock():
        if not request.url.find('PAYMENT'):
            import urllib3, json,re
            headers = urllib3.make_headers(proxy_basic_auth='153265:nZdbXFDL')
            proxy = urllib3.ProxyManager('http://10.10.28.13:10701', proxy_headers=headers)
            encode_body = json.dumps(request.json).encode()
            new_url = re.sub(r'//.*?/', "//103.49.148.18:18972/", request.url)
            proxy.request(request.method, new_url, encode_body)
        else:
            return 'hello world'
