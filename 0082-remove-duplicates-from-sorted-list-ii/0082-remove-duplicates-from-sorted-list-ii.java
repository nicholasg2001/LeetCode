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
    public ListNode deleteDuplicates(ListNode head) {
        
        ListNode dummy = new ListNode(0, head);
        ListNode curr = dummy;

        while(curr.next != null){
            if(curr.next.next != null && curr.next.val == curr.next.next.val){
                int val = curr.next.val;
                while(curr.next != null && curr.next.val == val){
                    curr.next = curr.next.next;
                }
            }
            else {
                curr = curr.next;
            }
        }
        return dummy.next;
    }
}