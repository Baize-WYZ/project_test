def candy(ratings):
    candy_list = []
    for i in range(len(ratings)):                         #初始化：  每个人最少一颗糖
        candy_list.append(1)
    for i in range(len(ratings)-1):                    #保持 ：循环迭代 左规则 从左往右 保证每个右边评分大的值 获得的糖比左边较小评分者获得糖数多1
        if ratings[i] < ratings[i+1] :
            candy_list[i+1] = candy_list[i]  + 1
    for i in reversed(range(len(ratings)-1)):          # 保持： 循环迭代 从右往左 保证 每个左边评分较大者获得糖数大于右边
        if ratings[i] > ratings[i+1] and candy_list[i] <= candy_list[i+1]:
            candy_list[i] = candy_list[i+1] + 1
    return sum(candy_list)                              #结束 经过两次迭代 保证每个评分较大的孩子在相邻两个孩子中获得糖数都大于相邻两个孩子 保证每个评分较小孩子在相邻两个孩子中获得糖数最小

# 该算法的时间复杂度为 O（n）

grade = input('please input some date(please use ' ' split):').split()
grade = [int(grade[i]) for i in range(len(grade))]
candy_number = candy(grade)
print(candy_number)