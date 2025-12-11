# Last updated: 12/10/2025, 11:36:56 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        group = defaultdict(list)
4
5        for s in strs:
6            count = [0] * 26
7            for ch in s:
8                count[ord(ch) - ord("a")] +=1
9            group[tuple(count)].append(s)
10        return list(group.values())
11
12            