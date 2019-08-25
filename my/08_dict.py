import importlib

hash_file = importlib.import_module("07_hash")


class Dict(hash_file.HashArray):
    def _iter_slot(self):
        for slot in self.array:
            if slot not in (hash_file.HashArray.EMPTY, hash_file.HashArray.UNUSED):
                yield slot

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        return self.get(key)

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value


def test_dict():
    import random
    import pytest

    d1 = Dict()
    d1['a'] = 1

    assert d1['a'] == 1
    assert d1.remove('a') == 1
    with pytest.raises(Exception) as info:
        # print(d1['a'])
        d1.remove('a')
    assert type(info.value) is KeyError

    l = list(range(10))
    random.shuffle(l)
    for i in l:
        d1.add(i, i)

    for i in range(10):
        assert d1.get(i) == i
    
    assert sorted(list(d1.keys())) == sorted(l)
