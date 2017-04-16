from heap_base import HeapBase


class Heap(HeapBase):
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        print i
        left = 2*i
        right = 2*i + 1
        size = len(self.heap)

        small = left if left < size and self.heap[left] < self.heap[i] else i
        small = right if right < size and self.heap[right] < self.heap[small] \
                else small

        if small != i:
            print size, i, small
            self.heap[i], self.heap[small] = self.heap[small], self.heap[i]
            self.heapify(small)

    def insert(self, value):
        self.heap.append(value)

        for i in xrange(len(self.heap)/2, 0, -1):
            self.heapify(i)
        print self.heap

