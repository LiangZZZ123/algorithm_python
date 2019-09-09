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

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        # for item in self._items:
        #     yield item
        return iter(self._items)


def test_array():
    a = Array(10)
    a[0] = 1
    assert a[0] == 1

    a.clear()
    assert a[0] is None


if __name__ == "__main__":
    a1 = Array(10)
    # # print([*a1])
    # # print([*iter(iter(a1)))])
    # a2 = Array(10)
    # a3 = Array(10)
    # print(f"a2:{id(a2)}, a3:{id(a3)}")

    # # notice a3 here is destroyed immediately after called id(Array(10)), and then a4 use a3's memory address
    # print(f"a3:{id(Array(10))}, a4:{id(Array(10))}")

    # iter_a1 = iter(a1)
    # print(iter_a1 is iter(iter_a1))
    # print(iter(a1) == iter(iter(a1)), id(a1), id(iter(a1)), id(iter(iter(a1))))


    from dis import dis
    
    dis('iter(a1)')