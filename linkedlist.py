from copy import deepcopy

from ll_base import LinkedListBase


class Node(LinkedListBase):

    def __init__(self, data):
        self.data = data
        self.next = None

    def setData(self, data):
        self.data = data

    def setNext(self, nxt):
        self.next = nxt

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        next = None
        prev = None
        current = self.head
        while not current.next:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def build(self):
        ptr = deepcopy(self.head)
        for i in xrange(10):
            if not self.head:
                self.head = Node(i)
                ptr = deepcopy(self.head)
            else:
                ptr.next = Node(i)
                ptr = ptr.next

