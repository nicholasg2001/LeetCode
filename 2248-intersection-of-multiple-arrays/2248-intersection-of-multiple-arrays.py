class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        ans = []
        for arr in nums:
            for num in arr:
                counts[num]+=1
        for i in counts:
            if counts[i] == len(nums):
                ans.append(i)
        return sorted(ans)
        