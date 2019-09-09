"""
Build a Queue and a Stack using collections.deque deque is basically a
    doubly-linked-list, which can be used for achieving both queue(FIFO)
    and stack(FILO)
So we can also do this by using "03_doubly_linked_list", we wil do this later
"""

from collections import deque


class queue_and_stack:
    def __init__(self):
        self.items = deque()

    def push(self, value):
        return self.items.append(value)

    # def appendleft(self, value):
    #     return self.items.appendleft(value)

    def pop(self):
        return self.items.pop()

    def popleft(self):
        return self.items.popleft()

    def __len__(self):
        return len(self.items)

    def clear(self):
        return self.items.clear()

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

    import pytest
    with pytest.raises(Exception) as info:
        q1.popleft()
    assert type(info.value) is IndexError

    # test for Stack
    s1 = queue_and_stack()
    s1.push(0)
    s1.push(1)
    s1.push(2)

    assert(len(s1)) == 3

    assert s1.pop() == 2
    assert s1.pop() == 1
    assert s1.pop() == 0
    