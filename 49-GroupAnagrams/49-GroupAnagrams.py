# Last updated: 11/18/2025, 8:56:57 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord("a")-ord(i)] +=1
            groups[tuple(count)].append(s)
        return list(groups.values())