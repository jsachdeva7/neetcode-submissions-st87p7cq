class Node:
    def __init__(self, key=-1, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node()
        self.right = Node()
        self.left.nxt = self.right
        self.right.prev = self.left

    def insert(self, node: Node) -> None:
        prevMRU = self.right.prev
        prevMRU.nxt = node
        node.prev = prevMRU
        node.nxt = self.right
        self.right.prev = node
        self.cache[node.key] = node

    def remove(self, node: Node):
        beforeNode = node.prev
        afterNode = node.nxt
        beforeNode.nxt = afterNode
        afterNode.prev = beforeNode
        del self.cache[node.key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) >= self.cap:
            self.remove(self.left.nxt)
        self.insert(Node(key, value))

        
