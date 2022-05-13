from collections import defaultdict
import heapq


class LFUCache:

    def __init__(self, capacity: int):
        self.dic = defaultdict(int)
        self.capacity = capacity
        self.count = 0
        self.heap = heapq.heapify()

    def get(self, key: int) -> int:
        return self.dic.get(key,-1)

    def put(self, key: int, value: int) -> None:
        # 失败！！！！！！：heapq不可行
        # 先插入
        # 不管是否已存在都插入
        if not self.dic[key]:
            heapq.heappush({key:1})
        self.dic[key] = value
        if self.count == self.capacity: # 已溢出，先删一个
            k,v = heapq.heappop(self.heap)
            del self.dic[k]
        else: #未溢出，计数加1
            self.count += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)