#初始化 数组flowerbed中无不符合种植规则的花
#保持  正向便利数组找出所有前向为0/null 的元素下标 后续便利找后向为0/null 的元素下标 重复部分为所找位置 从中去除原本为1的元素下标
#终止 两次遍历保证 找出的每项前后都无花束 即无争夺资源的花朵

def flowers_sort(flowerbed,number):
    after_moment = [flowerbed[0]]           #默认加入队列第一个元素
    before_moment = [flowerbed[len(flowerbed)-1]]  #默认加入队列最后一个元素
    the_moment = []
    x = []
    for i in range(1,len(flowerbed)):         #正序便利添加 前向为空或者空格的元素下标
        if flowerbed[i-1] == 0:
            after_moment.append(i)
    i = 0
    for i in  range(len(flowerbed)-1,0,-1):   #倒序便利 添加后项为空或者空格的元素下标
        if flowerbed[i] == 0:
            before_moment.append(i-1)
    the_moment = list(set(after_moment+before_moment))
    i = 0
    for i in range(len(the_moment)):
        if flowerbed[the_moment[i]] == 1:
            the_moment.pop(i)
    x = sum(the_moment)
    if number == x :
        print('true')
    else:
        print('false')


q = [1,0,0,0,1]
n = 1
flowers_sort(q,n)