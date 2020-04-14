# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# L={'Bob':75, 'Adam':92, 'Bart':66, 'Lisa':88}
#
# def get_keys(value1,dict1):
#     for key,value in dict1:
#         if value1==value:
#             return key
#
# def by_score(**dict1):
#     values_sorted=sorted(dict1.values())
#
#     new_dict={}
#
#     for value in values_sorted:
#         new_dict[get_keys(value,dict1)]=value
#
#     return new_dict
#
#
# L2 = sorted(L, key=by_score)
# print(L2)



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(info):
    return info[0]
print(sorted(L,key=by_name))



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(info):
    return info[1]
print(sorted(L,key=by_name,reverse=True))

