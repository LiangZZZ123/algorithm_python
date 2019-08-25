"""
hash table: refers to the structure comes with hash algorithm - mapping

hash-linked-list, open hashing:
  - easy to add/delete, o(1) all the time, save memory;
  - hard to search by value
hash-array, closed hashing:
  - easy to search by value, o(1);
  - add/delete is o(1) ~ o(n)(when linear/quadratic probing is need),
        and when there's no rehashing needed;
    Waste memory, waste resources when rehashing(reach load factor) is needed.
"""


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
    """
    We divide UNUSED and EMPTY because this is needed for bridging the probing
    """
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

    def _hash(self, key) -> int:
        return abs(hash(key)) % len(self.array)

    def _find_key(self, key):
        """
        :para
            key, the key of the key-value pair stored in the array
        :return
            index(int), the index of the position that the key-value pair stored in the array
            None, if the key is not found in the pair
        """
        index = self._hash(key)
        length = len(self.array)
        while self.array[index] is not HashArray.UNUSED:
            # When we intentionally make a Slot(None, None), it should not be a HashArray.Empty, and should continue search
            # if self.array[index] is HashArray.EMPTY:
            #     index = (index*5 + 1) % length
            #     continue
            if self.array[index].key == key and (not self.array[index] is HashArray.EMPTY):
                return index
            else:
                index = (index*5 + 1) % length
        else:
            return None

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        length = len(self.array)
        while not self._slot_can_insert(index):
            index = (index*5 + 1) % length
        return index

    def _slot_can_insert(self, index):
        return self.array[index] in (HashArray.UNUSED, HashArray.EMPTY)

    def __contains__(self, key):
        index = self._find_key(key)
        return index

    def add(self, key, value):
        """
        :para
            key, the key to be hashed
            value, the value that will be stored in that slot
        :return
            False, if the key already exists in the array, will refresh the paired value
            True, the new key-value pair has been successfully added in the array
        """
        if key in self:
            index = self._find_key(key)
            self.array[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self.array[index] = Slot(key, value)
            self.length += 1
            if self._load_factor >= 0.8:
                self._rehash()
            return True

    def _rehash(self):
        old_array = self.array
        new_size = len(self.array) * 2
        self.array = Array(new_size, HashArray.UNUSED)

        self.length = 0

        for slot in old_array:
            if slot not in (HashArray.UNUSED, HashArray.EMPTY):
                index = self._find_slot_for_insert(slot.key)
                self.array[index] = slot
                self.length += 1

    def get(self, key, default=None):
        """
        get是不会raise error的
        This method will return a default value if not find the key-value pair with the given key
        """
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self.array[index].value

    def __getitem__(self, key):
        """
        __getitem__是会raise error的
        实际上这是dict的魔术方法, _hash是不需要实现这个的
        The magic method of d1['xxx'],
        this method will raise KeyError if not find the key-value pair with the given key
        """
        index = self._find_key(key)
        if index is None:
            raise KeyError
        else:
            return self.array[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self.array[index].value
        self.array[index] = HashArray.EMPTY
        self.length -= 1
        return value

    def __iter__(self):
        for slot in self.array:
            if slot not in (HashArray.EMPTY, HashArray.UNUSED):
                yield slot.key


def test_hash_array():
    import pytest

    h1 = HashArray()
    h1.add('a', 0)
    h1.add('b', 1)
    h1.add('c', 2)
    
    assert len(h1) == 3
    assert h1.get('a') == 0
    assert h1.get('c') == 2
    assert h1.get('aaa') is None
    with pytest.raises(Exception) as info:
        h1[None]
    assert type(info.value) is KeyError
    
    assert h1.remove('a') == 0
    assert h1.get('a') is None
    with pytest.raises(Exception) as info:
        h1['a']
    assert type(info.value) is KeyError
    assert sorted(list(h1)) == ['b', 'c']

    n = 10
    for i in range(n):
        h1.add(i, i)

    for i in range(n):
        assert h1.get(i) == i

    h2 = HashArray()
    # 注意此时是没有None-None pair 储存在hashmap里面的
    assert h2.get(None) is None
    with pytest.raises(Exception) as info:
        h2[None]
    assert type(info.value) is KeyError

    assert h2.get(False) is None
    with pytest.raises(Exception) as info:
        h2[False]
    assert type(info.value) is KeyError
