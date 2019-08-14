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


    print(request.params)
    return "Hello World!"

if __name__ =="__main__":
    run(host='localhost', port=8083, debug=True)