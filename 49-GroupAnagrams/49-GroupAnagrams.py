# Last updated: 1/21/2026, 6:01:30 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        groups = defaultdict(list)
4
5        for s in strs:
6            count = [0] * 26
7            for c in s:
8                count[ord(c) - ord("a")] +=1
9            groups[tuple(count)].append(s)
10        return list(groups.values())