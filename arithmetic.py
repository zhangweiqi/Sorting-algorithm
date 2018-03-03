# coding:utf-8


import random
from collections import deque
import time

def create_list():
    alist = []
    for i in range(1000):
        alist.append(random.randint(1,1000))
    return alist

#输出时间
def print_time():
    #print time.strftime('%H %M %S', time.localtime())
    print time.time()



#选择排序
def select_sort(alist):
    for i in range(len(alist)):
        for j in range(i+1, len(alist)):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist


#冒泡排序
def bubble_sort(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1,i,-1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
    return alist


#插入排序
def insert_sort(alist):
    if len(alist) == 1:
        return alist
    for i in range(1, len(alist)):
        #bubble
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
    return alist


#快速排序
def quick_sort(alist):
    less = []
    pivotlist = []
    more = []
    if len(alist) <= 1:
        return alist
    else:
        pivot = alist[0]
        for i in alist:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotlist.append(i)
        
        less = quick_sort(less)
        more = quick_sort(more)

        return less + pivotlist + more


#鸡尾酒排序（定向冒泡排序）
#def cocktail_sort(alist):
    






#归并排序
#将列表裂变为长度为1的列表
def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    #将两列已经排序好的列表合并起来
    def merge(left, right):
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(alist) //2)
    left = merge_sort(alist[:middle])
    right = merge_sort(alist[middle:])
    return merge(left, right)
    



#希尔排序
def shell_sort(alist):
    n = len(alist)
    #初始步长
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            #每个步长进行插入排序
            temp = alist[i]
            j = i
            #插入排序
            while j >= gap and alist[j - gap] > temp:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = temp
        #得到新的步长
        gap = gap // 2
    return alist


alist = create_list()

print "************************************"
print_time()
print '原始序列' , alist
print_time()
print "************************************"
print_time()
print '选择排序' , select_sort(alist)
print_time()
print "************************************"
print_time()
print '冒泡排序' , bubble_sort(alist)
print_time()
print "************************************"
print_time()
print '插入排序' , insert_sort(alist)
print_time()
print "************************************"
print_time()
print '快速排序' , quick_sort(alist)
print_time()
print "************************************"
print_time()
print '归并排序' , merge_sort(alist)
print_time()
print "************************************"
print_time()
print '希尔排序', shell_sort(alist)
print_time()
print "************************************"
