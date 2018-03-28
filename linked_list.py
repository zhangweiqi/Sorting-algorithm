#!/usr/bin/python
# coding: utf-8

__Author__ = "Weiqi Zhang"
__LastUpdate__ = "2018.3.28"
__Declare__ = "结点和链表都用类表示，一层一层嵌套表示"


class Node(object):
    def __init__(self, value, pointer=0):
        self.data = value
        self.next = pointer


class LinkList(object):
    def __init__(self):
        self.head = 0

    def initlist(self, data):
        self.head = Node(data[0])
        temp = self.head
        for i in data[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def length(self):
        p = self.head
        length = 0
        while p != 0:
            length += 1
            p = p.next
        return length

    def empty(self):
        if self.length() == 0:
            return True
        else:
            return False

    def clear(self):
        self.head = 0

    def append(self, item):  # append item in the end of LinkList
        new_node = Node(item)
        if self.head == 0:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != 0:
                temp = temp.next
            temp.next = new_node

    def getitem(self, index):  # index is the No.number of the Linked_list
        if self.empty():
            print 'LinkList is empty.'
            return None
        elif index < 0 or index >= self.length():
            print 'The index is out of the LinkList.'
            return None

        counter = 0
        temp = self.head

        while temp.next != 0 and counter < index:
            temp = temp.next
            counter += 1

        if counter == index:
            return temp.data
        else:
            print 'target is not exist!'

    def insert(self, index, item):  # insert item in the middle of the LinkList

        if self.empty():
            print 'LinkList is empty.'
            return None
        elif index > self.length():
            print 'The index is out of the LinkList.'
            return None

        if index == 0:
            self.head = Node(item, self.head)
            return None

        temp = self.head
        for i in range(index - 1):
            temp = temp.next

        if temp.next == 0:
            temp.next = Node(item)
        else:
            old_item = temp.next
            temp.next = Node(item)
            temp.next.next = old_item
        return None

    def delete(self, index):

        if self.empty() or index < 0 or index >= self.length():
            print 'Index is out of the range'
            return None

        if index == 0:
            self.head = self.head.next

        temp = self.head
        for i in range(index - 1):
            temp = temp.next

        if temp.next.next == 0:
            temp.next = 0
        else:
            temp.next = temp.next.next

    def index(self, value):

        if self.empty():
            print 'LinkList is empty.'
            return None

        temp = self.head
        counter = 0
        while temp.next != 0:
            if temp.data == value:
                return counter
            counter += 1
            temp = temp.next
        return 'No value!'
