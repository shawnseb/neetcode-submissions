# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        return self.reverseHelp(None, head)


    def reverseHelp(self, prev: Optional[ListNode], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            head.next = prev
            return head
        copy = ListNode(head.val, head.next)
        copy.next = prev
        x = self.reverseHelp(copy, head.next);
        return x

        