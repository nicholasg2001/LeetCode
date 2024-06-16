class Node:
    def __init__(self, key=0, val=0):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        
        prev, next = self.tail.prev, self.tail
        prev.next = next.prev = node
        node.prev = prev
        node.next = next


    def remove(self, node):

        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            LRU = self.head.next
            self.remove(LRU)
            del self.cache[LRU.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)