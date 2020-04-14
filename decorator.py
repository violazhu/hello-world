import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

def log_param(param):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('begin call %s():' % func.__name__)
            result=func(*args, **kwargs)
            print('after call %s():' % func.__name__)
            return result
        return wrapper
    return decorator


def log_any_param(argv):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('begin call %s():' % func.__name__)
            result = func(*args, **kwargs)
            print('after call %s():' % func.__name__)
            return result
            return wrapper
        return decorator

    if type(argv)!=str:
        return decorator(argv)
    else:
        return decorator

@log_any_param
def now():
    print('2015-3-25')


if __name__ == "__main__":
    now()
    # func=now
    # print(now.__name__)
    # log('str')(now)()
    # log(now)()




# _*_ coding: utf-8 _*_

import functools

def log(argv):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('This is decorator')
            if type(argv) == str:
                print('show %s' % argv)
            return func(*args, **kw)
        return wrapper

    if type(argv) == str:
        return deco
    else:
        return deco(argv)

@log
def f():
    print('do f')

f()#log(f)()


@log('execute')
def f1():
    print('do f1')

f1()#log('execute')(f1)()