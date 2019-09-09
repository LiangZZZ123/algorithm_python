import importlib

hash_file = importlib.import_module('07_hash')


class Set(hash_file.HashArray):
    """
    Intersection: &
    Union: |
    Difference: -
    Symmetric difference: ^
    """
    def add(self, key):
        # a set is essentially a dict, we just make the value=True all the time
        return super().add(key, True)

    def __and__(self, other):
        """Intersection"""
        s1 = Set()
        for x in self:
            if x in other:
                s1.add(x)
        return s1

    def __or__(self, other):
        """Union"""
        s1 = Set()
        for x in self:
            s1.add(x)
        for x in other:
            s1.add(x)
        return s1

    def __sub__(self, other):
        """Difference"""
        s1 = Set()
        for x in self:
            if x not in other:
                s1.add(x)
        return s1

    def __xor__(self, other):
        """symmetric_difference"""
        return self.__or__(other) - self.__and__(other)


def test_set():
    # assert 0
    s1 = Set()
    s1.add(1)
    s1.add(2)
    s1.add(3)
    assert 1 in s1

    s2 = Set()
    s2.add(3)
    s2.add(4)
    s2.add(5)

    assert sorted(list(s1 & s2)) == [3]
    assert sorted(list(s1 - s2)) == [1, 2]
    assert sorted(list(s2 - s1)) == [4, 5]
    assert sorted(list(s1 | s2)) == list(range(1, 6))
    assert sorted(list(s1 ^ s2)) == [1, 2, 4, 5]
