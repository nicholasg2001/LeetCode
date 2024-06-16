# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        
        '''

        D -> 1 -> 2 -> 3 -> 4 -> 5
        L    R 
        

        '''

        length = 0

        getLength = head

        while getLength:
            getLength = getLength.next
            length+=1
        
        dummy = ListNode(0, head)
        front = dummy
        back = dummy
        for i in range(k-1):
            front = front.next
        
        for i in range(length-k):
            back = back.next
  

        temp = front.next.val
        front.next.val = back.next.val
        back.next.val = temp

        return dummy.next