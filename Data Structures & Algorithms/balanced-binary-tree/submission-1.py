# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def count(node: Optional[TreeNode], track: int)-> (bool, int):
            if not node:
                return (True,track)
            check1, countLeft = count(node.left, track + 1)
            check2, countRight = count(node.right, track + 1)
            if not check1 or not check2 or math.fabs(countLeft - countRight) > 1:
                return (False, -1)
            return (True, max(countLeft, countRight))
        
        ans, waste = count(root, 0)
        return ans

        