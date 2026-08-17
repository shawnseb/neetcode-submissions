# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answers = dict()
        
        def preOrderTraversal(root: Optional[TreeNode], depth: int):
            if not root:
                return
            answers[depth] = root.val
            preOrderTraversal(root.left, depth+1)
            preOrderTraversal(root.right, depth + 1)
        preOrderTraversal(root, 0)
        fin = []
        for a in answers:
            fin.append(answers[a])
        return fin


            
        