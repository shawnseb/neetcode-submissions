# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.answer = []
        self.trick(root, 0)
        return self.answer

    def trick(self, root: Optional[TreeNode], index) -> None:
        if not root:
            return
        if len(self.answer) <= index:
            self.answer.append([])
        self.answer[index].append(root.val)
        self.trick(root.left, index + 1)
        self.trick(root.right, index + 1)



        