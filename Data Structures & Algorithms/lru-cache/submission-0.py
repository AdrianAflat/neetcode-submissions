class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None

class LRUCache:

    # double linked list to keep track of last used item
    # hashmap to store values for fast lookup 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : node

        self.left = Node(0, 0)   # LRU end
        self.right = Node(0, 0)  # MRU end

        self.left.next = self.right
        self.right.prev = self.left

    # removes a node  
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    #inserts node at right end
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
