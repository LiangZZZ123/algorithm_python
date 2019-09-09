# Build LRUCache using dict and doubly-linked-list
# Achieve the OrderedDict by myself


class Node():
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None

class LRUCache():
    def __init__(self, capacity: int = 10):
        """
        head, tail永远存在, 且永远是两个empty node.
        这是doubly_linked_list的另一种实现, 与03_doubly-linked_list的实现略有不同, 但效果一样
        """
        self.cache = {}
        # self.size = 0
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Always add the node to the head"""
        old_head_node = self.head.next

        self.head.next = node
        node.previous = self.head
        node.next = old_head_node
        old_head_node.previous = node

    def _remove_node(self, node):
        """Suppose the sequence is (n1, node, n3)"""
        n1 = node.previous
        n3 = node.next
        n1.next = n3
        n3.previous = n1

    def _move_to_head(self, node):
        """
        When a node is used, move this node to head
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        When the cache exceeds the capacity, remove the last node in doubly-linked-list
        """
        tail_node = self.tail.previous
        self._remove_node(tail_node)
        return tail_node

    def get(self, key):
        node = self.cache.get(key, None)
        if node is None:
            return -1

        self._move_to_head(node)

        return node.value
        
    def put(self, key: int, value) -> None:
        node = self.cache.get(key)

        # If the key-value pair to be put in is not already in the cache, then put in that node
        if node is None:
            node = Node(key, value)
            self.cache[key] = node  # Add new node to dict
            self._add_node(node)  # Add new node to doubly-linked-list

            if len(self.cache) > self.capacity:
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]

        # Else, update the node value, and push that node to the head
        else:
            node.value = value
            self._move_to_head(node)


def test_LRUCache():
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    assert c.get(1) == 1
    c.put(4, 4)
    assert c.get(1) == 1
