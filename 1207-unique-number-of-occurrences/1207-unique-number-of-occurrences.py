class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)
        for num in arr:
            counts[num]+=1
        
        occurences = []
        for count in counts:
            if counts[count] in occurences:
                return False
            
            occurences.append(counts[count])
        return True
        