"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.known = dict()
        if not node:
            return None
        return self.clone(node)

        
    def clone(self, node: Optional['Node']) -> Optional['Node']:
        if node.val in self.known:
            return self.known[node.val]
        part = Node(node.val, [])
        ney = part.neighbors
        self.known[node.val] = part
        for i in node.neighbors:
            ney.append(self.clone(i)) 
        return part
        

        
        
        

        