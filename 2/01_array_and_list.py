class Array():
    def __init__(self, size=32):
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


def test_array():
    a1 = Array(10)
    a1[0] = 111
    assert a1[0] == 111

    a1.clear()
    for item in a1:
        assert item is None