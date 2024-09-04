# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left_prev = dummy
        curr = head

        for i in range(left-1):
            left_prev = left_prev.next
            curr = curr.next
        
        prev = None
        for i in range((right-left)+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        left_prev.next.next = curr
        left_prev.next = prev
        return dummy.next