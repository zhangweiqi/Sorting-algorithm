#!/usr/bin/env python
#! coding: utf-8

import random

def getrandomdata(num):
    alist = [random.randint(1,1000) for i in range(num)]
    return alist
    
# Bubble Sort
def bubble(alist):
    length = len(alist)
    for i in range(length-1,0,-1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1], alist[j]
    return alist
    
# Straight Select Sorting
def select(alist):
    length = len(alist)
    for i in range(length-1):
        for j in range(i+1,length):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist            
            
                


if __name__ == '__main__':
    num = int(raw_input("Please input the length of list(between 0,10000):"))
    alist = getrandomdata(num)
    bubblelist = bubble(alist)
    alist = getrandomdata(num)
    selectlist = select(alist)
       
    print "Bubblelist is ", bubblelist
    print "Selectlist is ", selectlist