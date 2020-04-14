from functools import reduce
print(type(reduce(lambda x,y:x+y,list(filter(lambda x:x!='.','123.456')))))


list1=list(range(2,5))



def is_odd(element):
    print(element)
    for i in range(2,element):
        if element%i != 0:
            return False
    return  True


print(list(filter(is_odd, range(2,100))))