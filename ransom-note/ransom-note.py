class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rNote = Counter(ransomNote)
        mag = Counter(magazine)
        
        for c in rNote:
            if mag[c] < rNote[c]:
                return False
            
        return True
        