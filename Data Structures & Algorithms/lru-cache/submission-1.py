class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # Maps key to Node
        
        # Dummy nodes to avoid edge cases with empty lists
        self.left = Node(0, 0)  # LRU side
        self.right = Node(0, 0) # MRU side
        
        # Connect dummy nodes initially
        self.left.next = self.right
        self.right.prev = self.left

    # Helper function: Removes a node from the linked list
    def remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper function: Inserts a node at the rightmost position (MRU)
    def insert(self, node: Node) -> None:
        prev_mru = self.right.prev
        
        prev_mru.next = node
        node.prev = prev_mru
        
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            # If it exists, update it to be most recently used
            node = self.map[key]
            self.remove(node)
            self.insert(node)
            return node.value
            
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # If the key already exists, remove the old node first
            self.remove(self.map[key])
            
        # Create a new node and add it to the map and MRU position
        new_node = Node(key, value)
        self.map[key] = new_node
        self.insert(new_node)
        
        # If we exceeded capacity, evict the Least Recently Used (LRU) node
        if len(self.map) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.map[lru_node.key]