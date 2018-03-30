#!/usr/bin/env python
# coding: utf-8

class Node(object):
    def __init__(self, initdata):
        self.__data = initdata
        self.__next = None

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, newnext):
        self.__next = newnext


class SinCycLinkedlist(object):
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(self.head)

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)

    def remove(self, item):
        prev = self.head
        while prev.getNext() != self.head:
            cur = prev.getNext()
            if cur.getData() == item:
                prev.setNext(cur.getNext())
            prev = prev.getNext()

    def search(self, item):
        pass

    #def empty(self):

    #def size(self):


if __name__ == '__main__':
    s = SinCycLinkedlist()
    print('s.empty() == %s, s.size() == %s' % (s.empty(), s.size()))
