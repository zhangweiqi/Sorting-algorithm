#!/usr/bin/env python
# coding: utf-8

class Queue(object):
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if self.queue != []:
            return self.queue.pop(0)
        else:
            return None
    
    def head(self):
        if self.queue != []:
            return self.queue[0]
        else:
            return None
            
    def tail(self):
        if self.queue != []:
            return self.queue[-1]
        else:
            return None
        
    def length(self):
        return len(self.queue)
        
    def empty(self):
        return self.queue == []
        
        