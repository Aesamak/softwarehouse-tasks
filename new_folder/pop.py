import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val)  

    def pop(self):
        if self.heap:
            return -heapq.heappop(self.heap)  
        return None

    def peek(self):
        return -self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def __str__(self):
        return str([-x for x in self.heap])  


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, val)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)



print("Max Heap Operations:")
max_heap = MaxHeap()
max_heap.push(10)
max_heap.push(30)
max_heap.push(20)
max_heap.push(5)
print("Max Heap:", max_heap)
print("Popped:", max_heap.pop())
print("Max Heap after pop:", max_heap)

print("\nMin Heap Operations:")
min_heap = MinHeap()
min_heap.push(10)
min_heap.push(30)
min_heap.push(20)
min_heap.push(5)
print("Min Heap:", min_heap)
print("Popped:", min_heap.pop())
print("Min Heap after pop:", min_heap)
