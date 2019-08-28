import heapq

class TopK:  # time: o(klogn)
    def __init__(self, iterable, k):
        self.minheap = []
        self.capacity = k
        self.iterable = iterable

    def push(self, val):
        if len(self.minheap) >= self.capacity:
            min_val = self.minheap[0]
            if val < min_val:
                pass
            else:
                # 返回并且pop堆顶最小值，推入新的 val 值并调整堆
                heapq.heapreplace(self.minheap, val)
        else:
            heapq.heappush(self.minheap, val)
    
    def get_topk(self):
        """
        Push all the values in the iterable in to minheap,
        and let it filter and retain the minium 10 items
        """
        for val in self.iterable:
            self.push(val)
        return self.minheap

def test():
    import random
    l1 = list(range(1000))
    random.shuffle(l1)
    print(TopK(l1, 10).get_topk())

if __name__ == "__main__":
    test()