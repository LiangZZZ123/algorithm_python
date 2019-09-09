class Node():
    __slots__ = ('value', 'prev', 'next')

    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class CircularDoubleLinkedList():

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('full')
        node = Node(value=value)
        tailnode = self.tailnode() or self.root
    
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('full')
        node = Node(value=value)
        if self.root.next is self.root:
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1
    
    def remove(self, node):
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -=1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value    

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode

def test_double_link_list():
    dl1 = CircularDoubleLinkedList()
    assert len(dl1) == 0

    dl1.append(0)
    dl1.append(1)
    dl1.append(2)

    assert list(dl1) == [*range(3)]

    assert [node.value for node in dl1.iter_node()] == [0, 1, 2]
    assert [node.value for node in dl1.iter_node_reverse()] == [2, 1, 0]

    headnode = dl1.headnode()
    assert headnode.value == 0
    dl1.remove(headnode)
    assert len(dl1) == 2
    assert [node.value for node in dl1.iter_node()] == [1, 2]

    dl1.appendleft(0)
    assert [node.value for node in dl1.iter_node()] == [0, 1, 2] 
