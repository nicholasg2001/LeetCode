/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    
    private ListNode reverse(ListNode head){
        ListNode prev=null;
        ListNode cur=head;
        ListNode next=head;

        while(next!=null){
            next=cur.next;
            cur.next=prev;
            prev=cur;
            cur=next;
        }

        return prev;
    }
    
    public void reorderList(ListNode head) {
        
        
        ListNode slow = head;
        ListNode fast = head.next;

        while(fast!=null && fast.next!=null){
            slow = slow.next;
            fast = fast.next.next;
        }
        
        ListNode left  = head;
        ListNode right = reverse(slow);
        ListNode nextL, nextR;
        while(left!=null && right!=null){
            nextL = left.next;
            left.next = right;
            nextR = right.next;
            right.next = nextL;
            left = nextL;
            right = nextR;
        }
        
    }
}