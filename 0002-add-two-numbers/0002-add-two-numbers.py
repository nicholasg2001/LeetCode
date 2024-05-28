# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0
        factor = 1
        
        while l1:
            count+= (l1.val * factor)
            l1 = l1.next
            factor*=10
        
        #reset factor
        factor = 1
        while l2:
            count+= (l2.val * factor)
            l2 = l2.next
            factor*=10
        
        #reset factor to get least significant digit         
        factor = 1
        l3 = ListNode((count // factor) % 10)
        head = l3
        factor*=10
        
        while(factor <= count):
    
            digit = (count // factor) % 10    
            head.next = ListNode(digit)
            head = head.next
            factor*=10
        
        
        return l3
        
        
        
        
            
        
        
        