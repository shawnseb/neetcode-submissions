# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and root:
            return True
        elif not subRoot:
            return False
        elif not root:
            return False
        return self.trace(root, subRoot)
    
     def trace(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False 
        if root.val == subRoot.val:
            if (self.isSameTree(root, subRoot)):
                return True
            else:
                return self.trace(root.left, subRoot) or self.trace(root.right, subRoot)

        else :
            return self.trace(root.left, subRoot) or self.trace(root.right, subRoot)
        



     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSameNode(p,q)
            
     def isSameNode(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q:
            if p.val == q.val:
                return self.isSameNode(p.left, q.left) and self.isSameNode(p.right, q.right)
            else:
                return False
        return False

        