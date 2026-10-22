# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def findIndice(obj):
            if obj == None:
                return 0
            num = findIndice(obj.next) + 1
            if num == n + 1:
                obj.next = obj.next.next
            return num
        fake = ListNode(0, head)
        gone = findIndice(fake)
        return fake.next
        
        