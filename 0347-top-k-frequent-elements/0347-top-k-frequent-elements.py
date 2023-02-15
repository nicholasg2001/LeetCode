class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 and k == 1:
            return nums
        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1
        
        
        sortedCount = dict(sorted(counts.items(), key = operator.itemgetter(1), reverse=True))
        ans = []
        for count in sortedCount:
            if len(ans) != k:
                ans.append(count)
                
        return ans
        
        
            
                              
        
        