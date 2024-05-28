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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode dummyHead = new ListNode(0);
        ListNode tail = dummyHead;
        
        int carry = 0;
        int digit;
        int digit1;
        int digit2;
        int sum;
        
        while(l1 != null || l2 != null || carry != 0){
            if(l1 != null){
                digit1 = l1.val;
            } else {
                digit1 = 0;           
            }
            if(l2 != null){
                digit2 = l2.val;
            } else {
                digit2 = 0;
            }
            
            sum = digit1 + digit2 + carry;
            digit = sum % 10;
            carry = Math.floorDiv(sum, 10);
            
            ListNode newNode = new ListNode(digit);
            tail.next = newNode;
            tail = tail.next;
            
            if(l1 != null){
                l1 = l1.next;
            } else {
                l1 = null;
            }
            if(l2 != null){
                l2 = l2.next;
            } else {
                l2 = null;
            }
        }
        ListNode result = dummyHead.next;
        dummyHead.next = null;
        return result;
    }
}