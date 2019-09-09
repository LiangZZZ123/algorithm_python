"""
Build queue_and_stack using "03_doubly_linked_list".
"""

import importlib

doubly_linked_list_file = importlib.import_module("03_doubly_linked_list")


class queue_and_stack(doubly_linked_list_file.DoublyLinkedList):
    # def __init__(self):
    #     self.items = doubly_linked_list_file.DoublyLinkedList()

    def push(self, value):
        return self.addright(value)

    # def appendleft(self, value):
    #     return self.items.addleft(value)

    def pop(self):
        return self.popright()

    # def popleft(self):
    #     return self.popleft()

    # def __len__(self):
    #     return len(self.items)

    # def clear(self):
    #     return self.items.clear()

def test_queue_and_stack():
    # test for Queue
    q1 = queue_and_stack()
    q1.push(0)
    q1.push(1)
    q1.push(2)

    assert len(q1) == 3

    assert q1.popleft() == 0
    assert q1.popleft() == 1
    assert q1.popleft() == 2

    assert list(q1) == []

    import pytest
    with pytest.raises(Exception) as info:
        q1.popleft()
    assert type(info.value) is IndexError

    q2 = queue_and_stack()
    q2.push(0)
    q2.push(1)
    q2.push(2)
    q2.clear()
    assert list(q2) == []

    # test for Stack
    s1 = queue_and_stack()
    s1.push(0)
    s1.push(1)
    s1.push(2)

    assert(len(s1)) == 3

    assert s1.pop() == 2
    assert s1.pop() == 1
    assert s1.pop() == 0
