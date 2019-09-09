"""
LinkedList: addleft, addright, popleft o(1)
            popright o(n), because must traverse to the second-last node

LinkedList是便于FIFO(addright, popleft)的o(1), 所以本身就是一个queue的最优实现


如果要做到LIFO的o(1),即stack的最优实现, 必须借助DoublyLinkedList. 
因为LinkedList的popright 是o(n)


Array: addright, popright, o(1), when the assigned memory block is not changed;
       addleft, popleft, add/pop in the middle, o(n)

Array在不扩容/缩容的情况下，LIFO(addright, popright)是o(1)
"""

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"<Node: value={self.value}, "


class LinkedList():
    """
    We regulate that there's no root points to headnode, when the linkedlist is empty,
    we just use head=None to represent.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def addright(self, value):  # o(1)
        node = Node(value)

        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def addleft(self, value):   # o(1)
        node = Node(value)

        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def __iter__(self):
        # for node in self.iter_factory():
        #     yield node.value
        return self.iter_factory()

    def iter_factory(self):
        current = self.head
        if len(self) > 0:
            # while current is not self.tail.next:
            for _ in range(len(self)):
                yield current
                # finally current will become none, then it should not have current.next
                if current is not None:
                    current = current.next

    def remove(self, value):    # o(1) if remove head, o(n) if remove tail
        if len(self) == 0:
            raise IndexError("this is an empty linkedlist, no node to remove")

        previous = self.head
        for current in self:
            if current.value == value:
                previous.next = current.next
                if current is self.head:
                    self.head = current.next
                if current is self.tail:
                    self.tail = previous
                del current
                self.length -= 1
                return 1
            else:
                previous = current
        return -1

    def popright(self):  # o(n)
        if len(self) == 0:
            raise Exception("Cannot pop from empty linkedlist")
        right = self.tail
        self.remove(right.value)
        return right.value

    def popleft(self):  # o(1)
        if len(self) == 0:
            raise Exception("Cannot pop from empty linkedlist")
        left = self.head
        self.remove(left.value)
        return left.value
    
    def find(self, value):  # o(n)
        """
        :para
            value: the value this node stores
        :return
            the index of this node, -1 if not found
        """
        index = 0
        for node in self:
            if node.value == value:
                return index
            index += 1
        return -1

    def clear(self):
        for node in self:
            del node
        self.head = None
        self.tail = None
        self.length = 0

    def reverse(self):
        if len(self) in (0, 1):
            return None

        n1 = None   # n1 represents the node before the headnode
        n2 = self.head
        self.tail = n2

        # head = self.switch_position(n1, n2)
        # print(f"head is {head}")
        # self.head = head
        while n2 is not None:
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3
        # print(n1, n2, n3)
        self.head = n1
     
        
def test():
    # assert 0
    import pytest
            
    # test __len__(), addright(value), addleft(value)
    l1 = LinkedList()
    l1.addright(0)
    l1.addright(1)
    l1.addright(2)
    l1.addright(3)
    l1.addleft(-1)
    l1.addleft(-2)
    assert len(l1) == 6
    assert [x.value for x in l1] == list(range(-2, 4))

    # test __iter__()
    l2 = LinkedList()
    assert [x.value for x in l2] == list()

    # test remove(value)
    l3 = LinkedList()
    for x in range(5):
        l3.addright(x)
    assert [x.value for x in l3] == list(range(5))
    l3.remove(0)
    l3.remove(2)
    l3.remove(4)
    assert [x.value for x in l3] == [1, 3]

    # test find(value)
    l4 = LinkedList()
    for x in range(5):
        l4.addright(x)
    assert l4.find(0) == 0
    assert l4.find(3) == 3
    assert l4.find(-1) == -1
    assert l4.find(6) == -1

    # Again: test remove(value)
    l5 = LinkedList()
    with pytest.raises(Exception) as info:
        l5.remove('aaa')
    l5.addright('aaa')
    l5.addright('bbb')
    l5.remove('bbb')
    assert [x.value for x in l5] == ['aaa']
    assert l5.remove('bbb') == -1
    assert l5.remove('aaa') == 1
    assert [x.value for x in l5] == []

    # test popright(), popleft()
    l6 = LinkedList()
    l6.addright('aaa')
    l6.addright('bbb')
    l6.addright('ccc')
    l6.addright('ddd')
    assert l6.popright().value == 'ddd'
    assert l6.popleft().value == 'aaa'
    assert [x.value for x in l6] == ['bbb', 'ccc']

    # test clear()
    l7 = LinkedList()
    l7.addright('1')
    l7.addright('2')
    l7.clear()
    assert len(l7) == 0
    assert [x.value for x in l7] == []

    # test reverse()
    # assert(0)
    l8 = LinkedList()
    for x in range(5):
        l8.addright(x)
    l8.reverse()
    assert [x.value for x in l8] == list(reversed(range(5)))


# l8 = LinkedList()
# for x in range(5):
#     l8.addright(x)
# l8.reverse()
# print(list(l8))
