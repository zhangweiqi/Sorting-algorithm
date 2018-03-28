# coding:utf-8


import random
from collections import deque
import time


def create_list():
    alist = []
    for i in range(1000):
        alist.append(random.randint(1, 1000))
    return alist


# ���ʱ��
def print_time():
    # print time.strftime('%H %M %S', time.localtime())
    print time.time()


# ѡ������
def select_sort(alist):
    for i in range(len(alist)):
        for j in range(i + 1, len(alist)):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
    return alist


# ð������
def bubble_sort(alist):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1, i, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
    return alist


# ��������
def insert_sort(alist):
    if len(alist) == 1:
        return alist
    for i in range(1, len(alist)):
        # bubble
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
    return alist


# ��������
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


# ��β�����򣨶���ð������
# def cocktail_sort(alist):


# �鲢����
# ���б��ѱ�Ϊ����Ϊ1���б�
def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    # �������Ѿ�����õ��б�ϲ�����
    def merge(left, right):
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(alist) // 2)
    left = merge_sort(alist[:middle])
    right = merge_sort(alist[middle:])
    return merge(left, right)


# ϣ������
def shell_sort(alist):
    n = len(alist)
    # ��ʼ����
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # ÿ���������в�������
            temp = alist[i]
            j = i
            # ��������
            while j >= gap and alist[j - gap] > temp:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = temp
        # �õ��µĲ���
        gap = gap // 2
    return alist


alist = create_list()

print "************************************"
print_time()
print 'ԭʼ����', alist
print_time()
print "************************************"
print_time()
print 'ѡ������', select_sort(alist)
print_time()
print "************************************"
print_time()
print 'ð������', bubble_sort(alist)
print_time()
print "************************************"
print_time()
print '��������', insert_sort(alist)
print_time()
print "************************************"
print_time()
print '��������', quick_sort(alist)
print_time()
print "************************************"
print_time()
print '�鲢����', merge_sort(alist)
print_time()
print "************************************"
print_time()
print 'ϣ������', shell_sort(alist)
print_time()
print "************************************"
