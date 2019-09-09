from collections import deque


GRAPH = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}

# FIFO


class Queue(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


bfs_list = []
def bfs(graph, start):
    q1 = Queue()
    q1.push(start)
    searched = set()
    while q1:
        cur_node = q1.pop()
        if cur_node not in searched:
            bfs_list.append(cur_node)
            searched.add(cur_node)
            for node in graph[cur_node]:
                q1.push(node)


print('bfs:')
bfs(GRAPH, 'A')
print(bfs_list)


# DFS_SEARCHED = set()
# def dfs(graph, start):
#     if start not in DFS_SEARCHED:
#         print(start)
#         DFS_SEARCHED.add(start)
#     for node in graph[start]:
#         if node not in DFS_SEARCHED:
#             dfs(graph, node)

def dfs(graph, start):
    DFS_SEARCHED = set()
    dfs_list = []

    def inner(graph, start):
        nonlocal DFS_SEARCHED, dfs_list
        if start not in DFS_SEARCHED:
            # print(start)
            dfs_list.append(start)
            DFS_SEARCHED.add(start)
        for node in graph[start]:
            if node not in DFS_SEARCHED:
                inner(graph, node)
    inner(graph, start)
    return dfs_list


print('dfs:')
print(dfs(GRAPH, 'A'))


# Achieve dfs using customized Stack built from deque
# LIFO
class Stack():
    def __init__(self):
        self._deque = deque()
    
    def push(self, value):
        return self._deque.append(value)
    
    def pop(self):
        return self._deque.pop()
    
    def __len__(self):
        return len(self._deque)


def dfs_use_stack(graph, start):
    dfs_list = []

    stack = Stack()
    stack.push(start)
    searched = set()
    while stack:
        cur_node = stack.pop()
        if cur_node not in searched:
            dfs_list.append(cur_node)
            searched.add(cur_node)
            # why add reversed here?
            for node in reversed(graph[cur_node]):
                stack.push(node)
    return dfs_list

print('dfs_use_stack:')
print(dfs_use_stack(GRAPH, 'A'))
