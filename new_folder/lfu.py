from collections import Counter

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  
        self.freq = Counter() 
         
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.freq[key] += 1  
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.cache:
            self.cache[key] = value
            self.get(key)  
            return
        
        if len(self.cache) >= self.capacity:
            lfu_key = min(self.freq, key=self.freq.get)  
            del self.cache[lfu_key]
            del self.freq[lfu_key]
        
        self.cache[key] = value
        self.freq[key] = 1

lfu = LFUCache(2)
print(lfu.freq)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))  
lfu.put(3, 3)      
print(lfu.get(2))  
print(lfu.get(3))  
lfu.put(4, 4)     
print(lfu.get(1))  
print(lfu.get(3))  
print(lfu.get(4))
print(lfu.freq)
