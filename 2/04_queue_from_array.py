class Array():
    def __init__(self, size=16):
        self._size = size
        self._items = [None] * size
    
    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self):
        for i in range(len(self._items)):
            self._items[i] = None
    
    def __iter__(self):
        for item in self._items:
            yield item


class ArrayQueue():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.head - self.tail

    def push(self, value):
        if len(self) >= self.maxsize:
            raise Exception('full')
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    
def test_array_queue():
    import pytest
    size = 5
    q1 = ArrayQueue(size)
    for i in range(size):
        q1.push(i)
    
    with pytest.raises(Exception) as info:
        q1.push(6)
    assert 'full' in str(info.value)

    assert len(q1) == 5

    assert q1.pop() == 0
    assert q1.pop() == 1

    assert len(q1) == 3

    q1.push(55)
    
    assert len(q1) == 4

    
