# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help(node: Optional[TreeNode], max: int, min: int) ->bool:
            if not node:
                return True
            if node.val >= max:
                return False
            if node.val <= min:  
                return False
            if node.left and node.val < node.left.val: 
                return False
            if node.right and node.val > node.right.val:
                return False
            return help(node.left, node.val, min) and help(node.right, max, node.val)
        if not root:
            return True
        return help(root, float('inf'), float('-inf')) 
        
        