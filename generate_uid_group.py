import time
def fun(max_num):
    #创建并打开文件
    file_name='file_' +str(int(time.time()))+'_'+str(max_num)
    file_path='/Users/haolingzhu/Desktop/' + file_name +'.txt'


    #生成 list生成器
    uid_list= (x for x in range(max_num))

    with open(file_path, 'w',encoding='utf-8') as f:
        for uid in uid_list:
            f.write(str(uid)+'\n')



def duplicat_fun(max_num):
    #创建并打开文件
    file_name='file_' +str(int(time.time()))+'_'+str(max_num)+'_'+'duplicate'+'.txt'
    file_path='/Users/haolingzhu/Desktop/' + file_name


    #生成 list生成器
    uid_list= (x for x in range(max_num))

    with open(file_path, 'w',encoding='utf-8') as f:
        for uid in uid_list:
            f.write(str(uid)+'\n')
            f.write(str(uid) + '\n')

duplicat_fun(100000)