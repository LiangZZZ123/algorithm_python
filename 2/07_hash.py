class Array():
    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size

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


class Slot():
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashArray():
    UNUSED = None
    EMPTY = Slot(None, None)

    def __init__(self):
        self.array = Array(8, init=HashArray.UNUSED)
        self.length = 0

    @property
    def _load_factor(self):
        return self.length / len(self.array)

    def __len__(self):
        return self.length

    def _hash(self, key):
        return abs(hash(key)) % len(self.array)

    def _find_key(self, key):
        index = self._hash(key)
        length = len(self.array)
        while self.array[index] is not HashArray.UNUSED:
