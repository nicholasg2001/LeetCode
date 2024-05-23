class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        if(len(nums) == 0):
            return 0
        
        nums = sorted(nums)
        l = 0
        r = len(nums) -1
        c = 0
        
        while l < r:
            if nums[l] + nums[r] < target:
                c+=r-l
                l+=1
            else:
                r-=1
        
        return c