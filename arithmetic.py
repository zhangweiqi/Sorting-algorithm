# coding:utf-8


import random


def create_list():
    alist = []
    for i in range(10):
        alist.append(random.randint(1,100))
    return alist


#—°‘Ò≈≈–Ú
def select_sort(alist):
    for i in range(len(alist)):
        for j in range(i+1, len(alist)):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist


#√∞≈›≈≈–Ú
def bubble_sort(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1,i,-1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
    return alist


#≤Â»Î≈≈–Ú
def insert_sort(alist):
    if len(alist) == 1:
        return alist
    for i in range(1, len(alist)):
        #bubble
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
    return alist

#º¶Œ≤æ∆≈≈–Ú£®∂®œÚ√∞≈›≈≈–Ú£©
def cocktail_sort(alist):






#πÈ≤¢≈≈–Ú
def merge_sort(alist):




alist = create_list()
print alist


print '—°‘Ò' , select_sort(alist)
print '√∞≈›' , bubble_sort(alist)
print '≤Â»Î' , insert_sort(alist)

