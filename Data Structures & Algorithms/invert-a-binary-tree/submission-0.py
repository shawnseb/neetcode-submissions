# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertSubTree(self, root: Optional[TreeNode] ) -> Optional[TreeNode]:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertSubTree(root.left)
        self.invertSubTree(root.right)
        return root
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertSubTree(root)

    
    
        