class Node:
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class MRUCache:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} 
        self.head = Node(None, None)  
        self.tail = Node(None, None)  
        self.head.next = self.tail  
        self.tail.prev = self.head  

    def _remove(self, node):
        
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node):
        
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key):
        
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)  
        self._add_to_tail(node)  
        return node.value

    def put(self, key, value):
        """Inserts a key-value pair into the cache."""
        if key in self.cache:
           
            self._remove(self.cache[key])
            del self.cache[key]

        if len(self.cache) >= self.capacity:
            
            mru_node = self.tail.prev
            self._remove(mru_node)
            del self.cache[mru_node.key]

        
        new_node = Node(key, value)
        self._add_to_tail(new_node)
        self.cache[key] = new_node

    def display(self):
        
        current = self.head.next
        while current != self.tail:
            print(f"({current.key}: {current.value})", end=" <-> ")
            current = current.next
        print("MRU")


cache = MRUCache(3)  
cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")
cache.display() 

cache.get(2)  
cache.display()  

cache.put(4, "D")  
cache.display() 
