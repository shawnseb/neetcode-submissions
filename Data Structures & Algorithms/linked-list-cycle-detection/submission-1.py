# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sets = set()
        sets.add(head)
        if head:
            head = head.next
        else:
            return False
        while head:
            if head in sets:
                return True
            sets.add(head)
            head = head.next
        return False

        