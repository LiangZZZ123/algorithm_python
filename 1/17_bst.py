# -*- coding: utf-8 -*-
# Remember here: when we say subtree, it is represented by its root node,
#   and the node is represented by the node's key
# 下面BST class中的所有subtree指的其实是一个node， 而那个node又是以node's key来表示的


class BSTNode(object):
    def __init__(self, key, value, left=None, right=None):
        self.key, self.value, self.left, self.right = key, value, left, right


class BST(object):
    def __init__(self, root=None):
        self.root = root  # self.root represents the whole tree

    @classmethod
    def build_from(cls, node_list):
        cls.size = 0
        # The BST is stored in a key-node dict, and node are connected to other node
        key_to_node_dict = {}
        for node_dict in node_list:
            key = node_dict['key']
            key_to_node_dict[key] = BSTNode(key, value=key)   # 这里值暂时用 和 key一样的

        for node_dict in node_list:
            key = node_dict['key']
            node = key_to_node_dict[key]
            if node_dict['is_root']:
                root = node
            # We can see here, building an BST needs an dict query o(1)
            node.left = key_to_node_dict.get(node_dict['left'])
            node.right = key_to_node_dict.get(node_dict['right'])
            cls.size += 1
        # Finally create the BST
        return cls(root)

    def _bst_search(self, subtree, key):
        """
        :param
            subtree = self.root, represents the whole tree
            key: the key of the node to be searched in the BST
        :return
            subtree: the key of the node to be searched
        """
        # no tree to search on
        if subtree is None:
            return None
        # the key I wanna search on is smaller than the root's key
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)
        elif key > subtree.key:
            return self._bst_search(subtree.right, key)
        # If the key matches the current subtree's root's key,
        # will return the root node of the current subtree
        else:
            return subtree

    def __contains__(self, key):
        """实现 in 操作符"""
        return self._bst_search(self.root, key) is not None

    def get(self, key, default=None):
        """Return the value of the root node of the current subtree"""
        node = self._bst_search(self.root, key)
        if node is None:
            return default
        else:
            return node.value

    def _bst_min_node(self, subtree):
        if subtree is None:
            return None
        # If there is no left-sub-tree, which means there's no node with smaller value
        elif subtree.left is None:   # 找到左子树的头
            return subtree
        else:
            return self._bst_min_node(subtree.left)

    def bst_min(self):
        node = self._bst_min_node(self.root)
        return node.value if node else None

    def _bst_insert(self, subtree, key, value):
        """ 插入并且返回根节点

        :param subtree:
        :param key:
        :param value:
        """
        # Ending condition of the recursion, last subtree's left/right node comes to None
        if subtree is None:   # 插入的节点一定是根节点，包括 root 为空的情况
            subtree = BSTNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bst_insert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bst_insert(subtree.right, key, value)
        return subtree

    def add(self, key, value):
        """
        First, check if the key of the node to be added is already exists,
        if existing-node is found, renew that node, and return False
        else, insert a new node and return True
        """
        node = self._bst_search(self.root, key)
        if node is not None:
            node.value = value
            return False
        else:
            self.root = self._bst_insert(self.root, key, value)
            self.size += 1
            return True

    def _bst_remove(self, subtree, key):
        """删除节点并返回根节点"""
        if subtree is None:
            return None
        elif key < subtree.key:
            subtree.left = self._bst_remove(subtree.left, key)
            return subtree
        elif key > subtree.key:
            subtree.right = self._bst_remove(subtree.right, key)
            return subtree
        # if key == subtree.key
        else:
            # 叶节点，返回 None 把其父亲指向它的指针置为 None(在下一次recursion return 中会发生 subtree。left = None),
            #   其父亲就是recursion的下一层return中的subtree,
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:  # 只有一个孩子
                if subtree.left is not None:
                    return subtree.left   # 返回它的孩子并让它的父亲指过去
                else:
                    return subtree.right
            else:  # 俩孩子，寻找后继节点替换，并删除其右子树的后继节点，同时更新其右子树
                successor_node = self._bst_min_node(subtree.right)
                subtree.key, subtree.value = successor_node.key, successor_node.value
                # 在原subtree的右子树中remove key==successor_node.key 的那个节点， 并自动排序右子树
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

    if __name__ == "__main__":
        pass
