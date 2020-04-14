def trim(s):
    if s==' '*len(s):
        return ''

    slice_min=0
    slice_max=len(s)-1
    for index in range(len(s)):
        if s[index] != ' ':
            slice_min=index
            break

    for index in range(len(s)-1,-1,-1):
        if s[index] != ' ':
            slice_max=index+1
            break

    return s[slice_min:slice_max]


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功7!')