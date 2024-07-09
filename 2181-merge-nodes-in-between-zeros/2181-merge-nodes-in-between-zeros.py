# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy
        left = head
        curr = head.next
        sum_ = 0

        while curr:
            if curr.val == 0:
                left.val = sum_
                prev = prev.next
                left = left.next
                sum_ = 0
                curr = curr.next
            else:
                sum_ += curr.val
                curr = curr.next
        
        prev.next = None
        return dummy.next
