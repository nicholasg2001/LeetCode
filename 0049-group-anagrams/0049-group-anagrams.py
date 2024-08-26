from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                #associate character with index via ASCII 
                count[ord(c) - ord('a')] += 1

            #make it a tuple because key has to be immutable
            key = tuple(count)
            anagrams_dict[key].append(s)
        
        return anagrams_dict.values()