from collections import OrderedDict

class LRUCache:
    """
    Every time you use the cache, the recently used item will be put in the last position.
    OrderedDict is a combination of dict and doubly-linked-list
    """
    def __init__(self, length: int):
        self.length = length
        self.dict = OrderedDict()

    def __len__(self):
        return self.length

    def get(self, key):
        if key not in self.dict:
            return -1
        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key, value):
        """
        This operation will ensure the new added key-value, no matter existing in LRUCache or not,
        be put at the first-in position
        """
        if key in self.dict:
            self.dict.pop(key)

        self.dict[key] = value
        if len(self.dict) > len(self):
            self.dict.popitem(last=False)


def test_LRUCache():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    assert c.get(1) == 1
    c.put(4, 4)
    assert c.get(1) == 1
