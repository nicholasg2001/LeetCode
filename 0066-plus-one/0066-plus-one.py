class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits)-1
        if digits[index] != 9:
            digits[index] +=1
            return digits
        else:
            digits = int("".join(map(str, digits)))
            digits +=1
            digits = list(map(int, str(digits)))
            return digits
        
