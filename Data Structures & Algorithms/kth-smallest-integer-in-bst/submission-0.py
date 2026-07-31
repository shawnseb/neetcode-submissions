# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Helper function to chop off the smallest node and return its value
        def pop_smallest(current_root):
            
            # Case 1: The root itself is the smallest (no left child exists)
            if not current_root.left:
                # The value is the root's value. 
                # The NEW root of the tree is whatever is to the right.
                return current_root.val, current_root.right
            
            # Case 2: The smallest node is further down the left branch
            parent = current_root
            
            # Traverse down until `parent.left` is the very last left node
            while parent.left.left:
                parent = parent.left
                
            # We found it! The smallest node is parent.left
            smallest_val = parent.left.val
            
            
            parent.left = parent.left.right
            
            
            return smallest_val, current_root

        
        
        answer = -1
        for _ in range(k):
            
            answer, root = pop_smallest(root)
            
        return answer