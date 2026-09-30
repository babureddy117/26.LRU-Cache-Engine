from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        
        # Move key to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Move to end if already exists
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # Remove least recently used item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Example
lru = LRUCache(3)
lru.put(1, 10)
lru.put(2, 20)
lru.put(3, 30)

print(lru.get(1))  # 10
lru.put(4, 40)     # Removes key 2
print(lru.cache)
