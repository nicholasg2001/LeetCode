# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        head = head.next
        sum_ = 0

        while head:
            if head.val == 0:
                curr.next = ListNode(sum_)
                curr = curr.next
                sum_ = 0
            sum_ += head.val
            head = head.next

        return dummy.next
