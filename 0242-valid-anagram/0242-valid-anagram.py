class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = defaultdict(int)
        countT = defaultdict(int)
        
        for c in s:
            countS[c]+=1
        for c in t:
            countT[c]+=1
            
        
        return countS == countT