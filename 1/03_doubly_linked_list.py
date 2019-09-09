class Node():
    def __init__(self, value=None, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next

    def __repr__(self):
        return f"<Node: value={self.value}, previous={self.previous.value}, next={self.next.value}"


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def addright(self, value):
        node = Node(value=value)
        if len(self) == 0:
            self.head = node
            self.tail = node
            node.previous = node
            node.next = node
        else:
            old_tail = self.tail
            old_tail.next = node
            node.previous = old_tail
            node.next = self.head
            self.head.previous = node
            self.tail = node
        self.length += 1

    def addleft(self, value):
        node = Node(value=value)
        if len(self) == 0:
            self.head = node
            self.tail = node
            node.previous = node
            node.next = node
        else:
            old_head = self.head
            old_head.previous = node
            node.next = old_head
            node.previous = self.tail
            self.tail.next = node
            self.head = node
        self.length += 1

    def remove(self, node):
        """Suppose the sequence is (n1, node, n3)"""
        if len(self) == 0:
            raise IndexError("this is an empty linkedlist, no node to remove")
        
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.previous

        n1 = node.previous
        n3 = node.next
        n1.next = n3
        n3.previous = n1
        self.length -= 1
        return node.value

    def popright(self):
        return self.remove(self.tail)

    def popleft(self):
        return self.remove(self.head)

    def __iter__(self):
        for node in self.iter_factory():
            yield node.value

    def iter_factory(self):
        current = self.head
        if len(self) > 0:
            for _ in range(len(self)):
                # print(current)
                yield current
                current = current.next

    def iter_factory_reverse(self):
        current = self.tail
        if len(self) > 0:
            for _ in range(len(self)):
                yield current
                current = current.previous

def test_doubly_linked_list():
    # assert 0
    l1 = DoublyLinkedList()
    assert len(l1) == 0

    l1.addright(0)
    assert list(l1) == [0]
    l1.addright(1)
    assert list(l1) == [0, 1]
    l1.addright(2)
    assert list(l1) == [0, 1, 2]
    l1.addleft(-1)
    l1.addleft(-2)

    assert len(l1) == 5
    assert list(l1) == [-2, -1, 0, 1, 2]
    assert [x.value for x in l1.iter_factory_reverse()] == [2, 1, 0, -1, -2]

    print(l1.head, l1.tail)
    assert l1.popleft() == -2
    assert l1.popright() == 2
    print(l1.head, l1.tail)
    assert list(l1) == [-1, 0, 1]

    l1.popright()
    l1.popright()
    l1.popright()
    assert list(l1) == []


if __name__ == "__main__":
    test_doubly_linked_list()
