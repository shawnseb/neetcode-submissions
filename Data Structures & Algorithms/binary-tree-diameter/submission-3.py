# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        print(self.findDepth(root.right, 1))
        answer = self.help(root)
        return answer
        
        

    def help(self, root: Optional[TreeNode])-> int:
        if not root:
            return 0
        answer = self.findDepth(root.left, 0) + self.findDepth(root.right, 0)
        lebron = self.help(root.left)
        ricky = self.help(root.right)
        if answer > lebron and answer > ricky:
            return answer
        return max(lebron, ricky)
    def findDepth(self, root: Optional[TreeNode], index: int)->int:
        if not root:
            print("h")
            return index
        index += 1
        if not root.left and not root.right: 
            print("i")
            return index
        print("j")
        
        return max(self.findDepth(root.left, index), self.findDepth(root.right, index))

            

    
        

        