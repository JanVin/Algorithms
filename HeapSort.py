"""
Build heap class then sort list
"""


class Heap():
    def __init__(self, array, heap_size):
        self.heap_size = heap_size - 1
        self.array = array
        self.largest = None

    def parent(self, num_id):
        return num_id // 2

    def left(self, num_id):
        return 2*num_id

    def right(self, num_id):
        return 2*num_id+1

    def max_heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if ((left <= self.heap_size) and (self.array[left] > self.array[i])):
            self.largest = left
        else:
            self.largest = i
        if (right <= self.heap_size) and (self.array[right] > self.array[self.largest]):
            self.largest = right
        if self.largest != i:
            self.array[i], self.array[self.largest] = self.array[self.largest], self.array[i]
            self.max_heapify(self.largest)

    def build_max_heap(self):
        number = self.heap_size
        print(number)
        for i in range(number//2, -1, -1):
            self.max_heapify(i)

    def sort(self):
        self.build_max_heap()
        for i in range(self.heap_size, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heap_size -= 1
            self.max_heapify(0)


list1 = [3, 5, 6, 1, 1, 13, 21, 31, 15, 16, 7, 10, 11, 22, 45, -3]
test1 = Heap(list1, 16)
test1.sort()
print(list1)
