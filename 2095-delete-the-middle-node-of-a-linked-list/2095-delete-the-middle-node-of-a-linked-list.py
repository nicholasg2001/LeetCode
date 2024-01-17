# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        if not fast.next.next:
            return None

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = middle.next

        return head
        