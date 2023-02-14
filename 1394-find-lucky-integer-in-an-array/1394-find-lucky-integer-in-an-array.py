class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckyNum = []
        counts = defaultdict(int)
        
        for num in arr:
            counts[num]+=1
        
        for num in counts:
            if counts[num] == num:
                luckyNum.append(num)
        
        if luckyNum:
            return max(luckyNum)
        else:
            return -1
        