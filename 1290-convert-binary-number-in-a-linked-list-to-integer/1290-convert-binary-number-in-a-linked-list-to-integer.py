# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        # val = []

        # while head:
        #     val.append(head.val)
        #     head = head.next
        # ans = 0
        # pos = 0 
        # for i in range(len(val)-1, -1, -1):
        #     ans+= val[i] * (2 ** pos)
        #     pos+=1
        # return ans

        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        pos = 0
        ans = 0
        while prev:
            ans+= prev.val * (2 ** pos)
            pos+=1

        return ans


