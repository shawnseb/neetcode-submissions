# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        index = 0
        sum = 0
        while l1 or l2:
            if l1:
                sum+=(10 ** index * l1.val)
                l1 = l1.next
            if l2: 
                sum+= 10 ** index * l2.val
                l2 = l2.next
            index = index + 1
        sum = sum
        funny = str(sum)
        self.final = None
        index = len(funny)
        print(sum)
        def help(number, index) -> Optional[ListNode]:
            if index == 0:
                self.final = ListNode(number, None)
                return self.final
            div = 10 ** index
            answer = number//div
            node = help(number - answer*div, index - 1)
            node.next = ListNode(answer, None)
            print(node.val)
            return node.next
        sum = int(sum)
        
        help(sum, index-1)
        
        return self.final
        



        