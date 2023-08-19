class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        maxEven = -1
        count = 0
        counts = defaultdict(int)
        
        for num in nums:
            if num % 2 == 0:
                counts[num] +=1
        for key, value in counts.items():
            if value > count:
                maxEven = key
                count = value
            if value == count and key < maxEven:
                maxEven = key
        return maxEven
        
        