
def eraseOverlapIntervals(intervals):
    '''
    初始化 设置第一个区间为总区间 即无重叠

    '''
    a = list(range(len(intervals)))
    count = 0
    if len(a)>1:
        a.remove(a[0])
        for j in a:   #
            key = intervals[j]
            x = j - 1
            while x >= 0 and intervals[x][-1] > key[-1]:
                intervals[x + 1] = intervals[x]
                x = x - 1
            intervals[x + 1] = key #
        minx = intervals[0]
        for i in a:
            if intervals[i][0] < minx[-1]:
                count = count + 1
            else:
                minx = intervals[i]
        return count
    else:
        return count

list_s = [[0,2],[1,3],[2,4],[3,5],[4,6]]
print(eraseOverlapIntervals(list_s))