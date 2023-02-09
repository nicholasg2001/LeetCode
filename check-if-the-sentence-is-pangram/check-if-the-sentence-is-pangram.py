class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set()
        for char in sentence:
            if char not in alphabet:
                alphabet.add(char)
            else:
                continue
        if len(alphabet) == 26:
            return True
        else:
            return False
        