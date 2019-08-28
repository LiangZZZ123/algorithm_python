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
        """Add to the tail, then do the _siftup"""
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count-1)

    def _siftup(self, index):
        if index > 0:
            parent = int((index-1) / 2)
            if self._elements[index] > self._elements[parent]:
                self._elements[index], self._elements[parent] = self._elements[parent], self._elements[index]
                self._siftup(parent)

    def extract(self):
        """
        Always extract the biggest item in the tree, which is the root node in MaxHeap,
        then put the tail node to the top, and rearrange the tree by doing _siftdown
        """
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
        if (left < self._count and  # has left-sub-node
                self._elements[left] >= self._elements[largest] and
                self._elements[left] >= self._elements[right]):
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        # If the top node is not the largest node, replace the top node with its left/right-sub-node
        if largest != index:
            self._elements[index], self._elements[largest] = self._elements[largest], self._elements[index]
            self._siftdown(largest)


def test_maxheap():
    import random
    n = 100
    h1 = MaxHeap(n)
    for i in range(n):
        h1.add(i)
    for i in reversed(range(n)):
        # do extract() on MaxHeap, should extract the biggest node in reverse order
        assert i == h1.extract()


def heap_sort_reverse(array):  # inplace, unstable, time:o(nlogn)
    """Our MaxHeap sort results in [10, 9, 8]"""
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    res = []
    for i in range(length):
        res.append(maxheap.extract())
    return res


def test_heap_sort_reverse():
    import random
    l1 = list(range(100))
    random.shuffle(l1)
    assert heap_sort_reverse(l1) == sorted(l1, reverse=True)


def heap_sort_use_heapq(iterable):
    """heapq is a MinHeap, sort results in [8, 9, 10]"""
    from heapq import heappush, heappop
    # To create a heap, use a list initialized to[],
    # or you can transform a populated list into a heap via function heapify().
    h1 = []
    for value in iterable:
        heappush(h1, value)
    return [heappop(h1) for i in range(len(h1))]


def test_heapsort_use_heapq():
    import random
    l1 = list(range(100))
    random.shuffle(l1)
    assert heap_sort_use_heapq(l1) == sorted(l1)
