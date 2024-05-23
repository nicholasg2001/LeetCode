class Solution:
    
    
    def reversePrefix(self, word: str, ch: str) -> str:
        
        l = 0
        for i in range(len(word)):
            
            if word[i] == ch:
                while(l < i):
                    word = list(word)
                    temp = word[l]
                    word[l] = word[i]
                    word[i]  = temp
                    l+=1
                    i-=1
                return "".join(word)
        
        return word
    
    def reverseString(word: str, l: int, r: int) -> str:            
            while(l < r):
                temp = word[l]
                word[l] = word[r]
                word[r] = temp
                r-=1
                l+=1

            return word
        

    
    
        