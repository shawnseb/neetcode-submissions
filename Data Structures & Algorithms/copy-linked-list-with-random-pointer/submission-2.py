"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.copied = dict()
        def help(copy: Optional[Node]) -> Optional[Node]:
            if not copy:
                return None
            if copy in self.copied:
                return self.copied[copy]
            ret = Node(copy.val, None, None)
            self.copied[copy] = ret
            ret.next = help(copy.next)
            ret.random = help(copy.random)
            return ret

        random = Node(0, None, None)
        random.next = help(head)
        return random.next
        