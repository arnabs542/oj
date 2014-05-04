'''
LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the
least recently used item before inserting a new item.
'''

class LRUCache:
    # @param capacity,an integer
    def __init__(self,capacity):
        self.cache = dict()
        self.capacity = capacity
        self.least = None

    # @return an integer
    def get(self,key):
        if self.cache.has_key(key):
            return self.cache[key]
        else:
            return -1

    # @param key,an integer
    # @param value,an integer
    # @return nothing
    def set(self,key,value):
        if len(self.cache) == self.capacity:
            for k,v in self.cache.items():
                if self.least == None:
                    self.least = k
                elif v < self.cache[self.least]:
                    self.least = k

            del(self.cache[self.least])
            self.cache[key] = value
        else:
            self.cache[key] = value

if __name__ == "__main__":
    c = LRUCache(1)
    c.set(2,1)
    print c.get(2)
    c.set(3,2)
    c.get(2)
    print c.get(3)

