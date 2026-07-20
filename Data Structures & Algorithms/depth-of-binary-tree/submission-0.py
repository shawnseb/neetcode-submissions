# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.help(root, 0)
    
    def help(self, root: optional[TreeNode], current: int) -> int:
        if not root:
            return current
        if not root.left and not root.right:
            return current + 1
        return max(self.help(root.left, current + 1), self.help(root.right, current+1))


        