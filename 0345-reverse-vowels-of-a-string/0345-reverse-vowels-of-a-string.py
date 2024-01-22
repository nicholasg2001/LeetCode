class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res = list(s)
        
        while(l <= r):
            if s[l] in vowels and s[r] in vowels:
                temp = res[l]
                res[l] = res[r]
                res[r] = temp
                l+=1
                r-=1
            elif s[l] in vowels and s[r] not in vowels:
                r-=1
            else:
                l+=1
        
        return ''.join(res)