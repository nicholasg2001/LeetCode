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
    
    public int calculateTwinSum(int[] arr, int i){
        int twin = arr.length - 1 - i;
        return arr[i] + arr[twin];
    }
    
    public int pairSum(ListNode head) {
        
        ListNode dummy = head;
        
        int count = 1;
        while(head.next != null){
            head = head.next;
            count++;
        }
        
        int[] arr = new int[count];
        int idx = 0;
        while(dummy != null){
            arr[idx] = dummy.val;
            dummy = dummy.next;
            idx++;
        }
        
        
        int max = 0;
        for(int i=0;i<arr.length;i++){
            int currSum = calculateTwinSum(arr, i);
            if(currSum > max){
                max = currSum;
            }
        }
        return max;
        
        
    }
}