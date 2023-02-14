class Solution:
    def frequencySort(self, s: str) -> str:
        counts = defaultdict(int)
        
        for c in s:
            counts[c]+=1
            
        descending = sorted(counts, key=counts.get, reverse=True)
        
        res = ""
        
        for char in descending:
            res += char*counts[char]
        return res
                
        