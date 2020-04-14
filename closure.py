""" 实现计数器统计函数调用次数 """


# def createCounter():
#     """ 方法1：list的原理类似C语言的数组和指针，不受作用域影响
#     直接改变值对应的地址。也就是说不是改变值的引用，而是永久改变值本身 """
#     L=0
#     def counter():
#         L=+1
#         return L
#     return counter

def createCounter1():
    """ 方法1：list的原理类似C语言的数组和指针，不受作用域影响
    直接改变值对应的地址。也就是说不是改变值的引用，而是永久改变值本身 """
    L=[0]
    def counter():
        print(L)
        print(L[0])
        L[0]+=1
        return L[0]
    return counter

def createCounter2():
    """ 方法2：使用global扩大变量作用域 """
    global n
    n=0
    def counter():
        global n
        n+=1
        return n
    return counter

def createCounter3():
    """ 方法3：使用nonlocal声明内层函数变量，使其能修改外层函数的变量 """
    n=0
    def counter():
        nonlocal n
        n+=1
        return n
    return counter

def createCounter4():
    """ 方法4：使用生成器在外层函数创建生成器对象，在内层函数调用next() """
    def count_generator():
        n=0
        while True:
            n+=1
            yield n
    # 调用生成器函数创建生成器对象一定要在外层函数进行
    temp=count_generator()

    def get_num():
        return next(temp)
    return get_num



# 测试:
counterA = createCounter1()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter1()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')