L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() if isinstance(x,str) else x for x in  L1]
print(L2)
