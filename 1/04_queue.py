# build Queue from "02_linked_list"

import importlib

linked_list_module = importlib.import_module('02_linked_list')


class EmptyError(Exception):
    pass


class Queue():
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.linked_list = linked_list_module.LinkedList()

    def __len__(self):
        return len(self.linked_list)

    def push(self, value):
        return self.linked_list.addright(value)

    def pop(self):
        if len(self) <= 0:
            raise EmptyError('the queue is already empty')
        return self.linked_list.popleft()


def test_queue():
    q1 = Queue()
    q1.push(0)
    q1.push(1)
    q1.push(2)

    assert len(q1) == 3

    assert q1.pop() == 0
    assert q1.pop() == 1
    assert q1.pop() == 2
    assert len(q1) == 0

    import pytest
    with pytest.raises(EmptyError) as info:
        q1.pop()
    assert 'empty' in str(info.value)
