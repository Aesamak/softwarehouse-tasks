import heapq

class MedianHeap:
    def __init__(self):
        self.max_heap = []  
        self.min_heap = []  
        self.del_map = {}  
    
    def insert(self, x):
        if not self.max_heap or x <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -x)  
        else:
            heapq.heappush(self.min_heap, x)
        self.rebalance()
    
    def delete(self, x):
        if x in self.del_map:
            self.del_map[x] += 1
        else:
            self.del_map[x] = 1
        self.lazy_cleanup()

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

    def rebalance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def lazy_cleanup(self):
        while self.max_heap and -self.max_heap[0] in self.del_map:
            val = -heapq.heappop(self.max_heap)
            self.del_map[val] -= 1
            if self.del_map[val] == 0:
                del self.del_map[val]
        
        while self.min_heap and self.min_heap[0] in self.del_map:
            val = heapq.heappop(self.min_heap)
            self.del_map[val] -= 1
            if self.del_map[val] == 0:
                del self.del_map[val]

        self.rebalance()


median_heap = MedianHeap()
median_heap.insert(10)
median_heap.insert(20)
median_heap.insert(30)
print(median_heap.find_median())  
median_heap.delete(20)
print(median_heap.find_median()) 
