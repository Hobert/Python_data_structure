# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#stack.py

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    def __repr__(self):
        l = len(self)*7
        s = "|"+"-"*l + ")\n|"
        for a in self:
            s+="| %-5s"%a#这一句有点懵
        s+="\n|" + "-" *l+")"
        return s
    __str__ = __repr__
