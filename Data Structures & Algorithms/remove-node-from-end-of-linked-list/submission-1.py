# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        copy = head
        index = self.findIndex(head, n)
        if index == 0:
            return None
        if n > index:
            return None
        if index -n == 0:
            return head.next
        for i in range(index-n - 1):
            head = head.next
        print(head.val)
        temp = head.next
        if not temp:
            return None
        head.next = temp.next
        return copy
        
    def findIndex(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = 0
        while head:
            head = head.next
            p = p+1
        return p

        