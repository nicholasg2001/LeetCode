# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        length = 0
        
        get_length = head

        while get_length:
            get_length = get_length.next
            length+=1
        
        left = ListNode(0, head)
        right = ListNode(0, head)

        for i in range(k-1):
            left = left.next
        for i in range(length-k):
            right = right.next
        
        temp = left.next.val
        left.next.val = right.next.val
        right.next.val = temp
        return head