class BSTNode():
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST():
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, nodes_list):
        cls.size = 0
        key_to_node_dict = {}
        for node_dict in nodes_list:
            key = node_dict['key']
            key_to_node_dict[key] = BSTNode(key, value=key)

        for node_dict in nodes_list:
            key = node_dict['key']
            node = key_to_node_dict[key]
            if node_dict['is_root']:
                root = node
            node.left = key_to_node_dict.get(node_dict['left'])
            node.right = key_to_node_dict.get(node_dict['right'])
            cls.size += 1
        return cls(root)

    def _bst_search(self, subtree, key):
        if subtree is None:
            return None
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)
        elif key > subtree.key:
            return self._bst_search(subtree.right, key)
        else:
            return subtree

    def __contains__(self, key):
        return self._bst_search(self.root, key) is not None

    def get(self, key, default=None):
        node = self._bst_search(self.root, key)
        if node is None:
            return default
        else:
            return node.value

    def _bst_min_node(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bst_min_node(subtree.left)

    def bst_min(self):
        node = self._bst_min_node(self.root)
        return node.value if node else None

    def _bst_insert(self, subtree, key, value):
        if subtree is None:
            subtree = BSTNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bst_insert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bst_insert(subtree.right, key, value)
        return subtree

    def add(self, key, value):
        node = self._bst_insert(self.root, key, value)
        if node is not None:
            node.value = value
            return False
        else:
            self.root = self._bst_insert(self.root, key, value)
            self.size += 1
            return True

    def _bst_remove(self, subtree, key):
        if subtree is None:
            return None
        elif key < subtree.key:
            subtree.left = self._bst_remove(subtree.left, key)
            return subtree
        elif key > subtree.key:
            subtree.right = self._bst_remove(subtree.right, key)
            return subtree
        elif key == subtree.key:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor_node = self._bst_min_node(subtree.right)
                subtree.key, subtree.value = successor_node.key, successor_node.value
                subtree.right = self._bst_remove(
                    subtree.right, successor_node.key)
                return subtree

    def remove(self, key):
        assert key in self
        self.size -= 1
        return self._bst_remove(self.root, key)


NODE_LIST = [
    {'key': 60, 'left': 12, 'right': 90, 'is_root': True},
    {'key': 12, 'left': 4, 'right': 41, 'is_root': False},
    {'key': 4, 'left': 1, 'right': None, 'is_root': False},
    {'key': 1, 'left': None, 'right': None, 'is_root': False},
    {'key': 41, 'left': 29, 'right': None, 'is_root': False},
    {'key': 29, 'left': 23, 'right': 37, 'is_root': False},
    {'key': 23, 'left': None, 'right': None, 'is_root': False},
    {'key': 37, 'left': None, 'right': None, 'is_root': False},
    {'key': 90, 'left': 71, 'right': 100, 'is_root': False},
    {'key': 71, 'left': None, 'right': 84, 'is_root': False},
    {'key': 100, 'left': None, 'right': None, 'is_root': False},
    {'key': 84, 'left': None, 'right': None, 'is_root': False},
]


def test_bst_tree():
    b1 = BST.build_from(NODE_LIST)
    for node_dict in NODE_LIST:
        key = node_dict['key']
        assert b1.get(key) == key
    assert b1.size == len(NODE_LIST)
    assert b1.get(-1) is None

    assert b1.bst_min() == 1

    b1.add(-1, -1)
    assert b1.bst_min() == -1

    b1.remove(12)
    assert b1.get(12) is None
