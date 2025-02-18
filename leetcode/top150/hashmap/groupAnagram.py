from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagramMap:
                anagramMap[key] = []
            anagramMap[key].append(s)
        return list(anagramMap.values())