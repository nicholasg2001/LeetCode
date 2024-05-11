class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // Initialize pointers for nums1, nums2, and the end of nums1
        int i = m - 1;
        int j = n - 1; 
        int k = m + n - 1;
        
        // Merge the arrays from the end to the beginning
        while (j >= 0) { 
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--]; // Copy the larger element from nums1
                /*
                same thing as nums1[k] = nums1[i];
                k--;
                i--;
                */
            } else {
                nums1[k--] = nums2[j--]; // Copy the element from nums2
            }
        }
    }
}