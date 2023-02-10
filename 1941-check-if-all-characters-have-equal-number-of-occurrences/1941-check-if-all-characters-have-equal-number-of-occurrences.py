class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c]+=1
    
        freq = counts.values()
        return len(set(freq))== 1
        
        
        