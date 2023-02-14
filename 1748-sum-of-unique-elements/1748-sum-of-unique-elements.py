class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1
        
        sum = 0
        for num in counts:
            if counts[num]==1:
                sum+=num
        return sum