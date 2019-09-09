"""
Design and implement a data structure for Least Frequently Used (LFU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key 
    if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
    When the cache reaches its capacity, it should invalidate the least frequently 
    used item before inserting a new item. For the purpose of this problem, 
    when there is a tie (i.e., two or more keys that have the same frequency), 
    the least recently used key would be evicted.
"""

import heapq


class LFUCache():

    def __init__(self, capacity):
        self.capacity = capacity
        self.time = 0             # total times this cache has been used
        self.map = {}             # key: value
        self.freq_time = {}       # key: (freq of that key, total time)
        # (freq, time, key), only updated when new key is added
        self.priority_queue = []
        # self.update = set()

    def get(self, key):
        self.time += 1

        if key in self.map:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time)
            # self.update.add(key)
            return self.map[key]
        return -1

    def put(self, key, value):
        if self.capacity <= 0:
            return None

        self.time += 1
        if not key in self.map:
            if len(self.map) >= self.capacity:
                while self.priority_queue and self.priority_queue[0]

    # 未完
