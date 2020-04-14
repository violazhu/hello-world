

from functools import reduce
def tonum(element):
    str='123.456'
    if element=='.':
        return 0
    # print(element)
    pow_index=pow(10, (str.index('.') - str.index(element)))
    # print(pow_index)
    return  int(element)*pow_index

print(list(map(tonum,'123.456')))

print(reduce(lambda x,y:x+y,[1000, 200, 30, 0, 0.4, 0.05, 0.006]))
print(reduce(lambda x,y:x+y,list(map(tonum,'123.456'))))



