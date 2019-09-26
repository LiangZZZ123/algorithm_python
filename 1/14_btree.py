# -*- coding: utf-8 -*-

from collections import deque


class Queue():
    def __init__(self):
        self._items = deque()

    def append(self, value):
        return self._items.append(value)

    def pop(self):
        return self._items.popleft()

    def empty(self):
        return len(self._items) == 0


class Stack(object):
    def __init__(self):
        self._items = deque()

    def push(self, value):
        return self._items.append(value)

    def pop(self):
        return self._items.pop()

    def empty(self):
        return len(self._items) == 0


class BinTreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinTree():
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """
        First put all nodes in to node_dict,
        then create connections between different nodes to form a tree
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)  # build and return the root node of this btree

    def preorder_trav(self, subtree):  # root - left - right
        if subtree is not None:
            print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

    def preorder_trav_use_stack(self, subtree):
        s = Stack()
        if subtree:
            s.push(subtree)
            while not s.empty():
                top_node = s.pop()
                print(top_node.data)
                if top_node.right:
                    s.push(top_node.right)
                if top_node.left:
                    s.push(top_node.left)

    def inorder_trav(self, subtree):  # left - root - right
        if subtree is not None:
            self.inorder_trav(subtree.left)
            print(subtree.data)
            self.inorder_trav(subtree.right)

    def reverse(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)

    def layer_trav(self, subtree):  # layer by layer
        """
        :param
            subtree: the root node of this tree
            current_nodes: nodes on the current layer
            next_nodes: nodes on the next layer
        """
        current_nodes = [subtree]
        next_nodes = []
        while current_nodes or next_nodes:
            for node in current_nodes:
                print(node.data)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            current_nodes = next_nodes
            next_nodes = []

    def layer_trav_use_queue(self, subtree):
        q = Queue()
        q.append(subtree)
        while not q.empty():
            cur_node = q.pop()
            print(cur_node.data)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)


node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]


btree = BinTree.build_from(node_list)
print('====先序遍历=====')
btree.preorder_trav(btree.root)

print('====使用 stack 实现先序遍历=====')
btree.preorder_trav_use_stack(btree.root)

print('====层序遍历=====')
btree.layer_trav(btree.root)

print('====用队列层序遍历=====')
btree.layer_trav_use_queue(btree.root)

btree.reverse(btree.root)
print('====反转之后的结果=====')
btree.preorder_trav(btree.root)
