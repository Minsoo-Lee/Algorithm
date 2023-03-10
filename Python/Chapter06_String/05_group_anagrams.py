# 49. Group Anagrams
import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = collections.defaultdict(list)
        
        for word in strs:
            result[''.join(sorted(word))].append(word)
        return list(result.values())