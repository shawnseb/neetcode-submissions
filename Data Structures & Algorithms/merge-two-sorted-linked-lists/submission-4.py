# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1 
        answer = ListNode()
        copy = answer
        while list1 and list2:
            if list1.val <= list2.val:
                copy.next=list1
                list1 = list1.next
                copy= copy.next
            else:
                copy.next=list2
                list2 = list2.next
                copy=copy.next
                
        if not list1:
                    copy.next = list2
                    return answer.next
        if not list2:
                    copy.next = list1
                    return answer.next
            
            
           
              
        
    
        