class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class MaxHeap():
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)  # count的第一个node是1， index的第一个node是0，

    def _siftup(self, index):
        if index > 0:
            parent = int((index - 1) / 2)
            if self._elements[index] > self._elements[parent]:
                self._elements[index], self._elements[parent] = self._elements[parent], self._elements[index]
                self._siftup(parent)
    
    def extarct(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if (left < self._count and
                self._elements[left] >= self._elements[largest] and  # why >= ?
                self._elements[left] >= self._elements[right]):
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != index:
            self._elements[index], self._elements[largest] = self._elements[largest], self._elements[index]
            self._siftdown(largest)


class PriorityQueue():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self, priority, value):
        # 注意这里把这个 tuple push进去，python 比较tuples的大小是先比较tuples中第一个元素的大小
        entry = (priority, value)
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extarct()
        if with_priority:
            return entry
        else:
            return entry[1]
        
    def is_empty(self):
        return len(self._maxheap) == 0


def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())
    assert res == ['purple', 'orange', 'black', 'white']
