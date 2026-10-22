# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        index = 0
        pack = deque()
        length = 1
        pack.append(root)
        answer = []
        if root == None:
            return answer
        while len(pack) != 0:
            item = pack.popleft()
            length -= 1
            if len(answer) <= index:
                answer.append([])
            answer[index].append(item.val)
            if item.left:
                pack.append(item.left)
            if item.right:
                pack.append(item.right)
            if length == 0:
                length = len(pack)
                index += 1
        return answer
            

            

        
        
    
        