# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        self.odd = 0
        self.size = 0
        reverse = self.findMiddle(head)
        if self.odd == 1:
            reverse = self.reverseLinkedList(reverse.next)
        else:
            reverse = self.reverseLinkedList(reverse)
        current = head
        copy = reverse
        nxt = None
        
        for i in range (self.size):
            nxt = current.next
           
            copy = reverse.next
            current.next = reverse
        
            current.next.next = nxt
            current = current.next.next
            reverse = copy
            
        current.next = None
            
        
            
        
        
        
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr= None,head
        if not head: 
            return head
        
        sixe = 0

        while curr :
            sixe = sixe + 1
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.size = sixe
        return prev
        





            
    def findMiddle(self, head: Optional[ListNode])-> Optional[ListNode]:
        slow, fast = head, head
        while fast is not None:
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                self.odd = 1
                return slow
        
        return slow

        