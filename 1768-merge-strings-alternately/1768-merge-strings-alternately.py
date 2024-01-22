class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # taking the lengths of both the words
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        j = 0
        # taking a string called output to store the new input
        output = ''
        # iterating across both the words
        while i < n1 or j < n2:
            if i < n1:
                output = output + word1[i]
                i = i + 1
            if j < n2:
                output = output + word2[j]
                j = j + 1

        return output
        
        