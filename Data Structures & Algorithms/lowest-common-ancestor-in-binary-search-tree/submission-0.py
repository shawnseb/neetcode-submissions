# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ancestors = []
        self.aggregate(root, p)
        print(self.ancestors)
        
        print(self.ancestors)
        pl = self.ancestors
        self.ancestors = []
        print(pl)
        self.aggregate(root, q)
        
        pr = self.ancestors
        print(pr)
        if len(pl) > len(pr):
            short = pr
            long = pl
        else:
            short = pl
            long = pr
        for i in short:
            if i in long:
                return i
        return None



    def aggregate(self, root: TreeNode, p: TreeNode) -> bool:
        print("hix")
        if not root:
            return False
        if root.val == p.val:
            self.ancestors.append(root)
            return True
        if self.aggregate(root.left, p) or self.aggregate(root.right, p):
            print("hi")
            self.ancestors.append(root)
            return True
        return False


        
        