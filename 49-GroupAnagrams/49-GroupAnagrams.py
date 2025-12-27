# Last updated: 12/26/2025, 11:27:20 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        groups = defaultdict(list)
4
5        for s in strs:
6            count = [0] * 26
7            for i in s:
8                count[ord(i) - ord("a")] +=1
9            groups[tuple(count)].append(s)
10        return list(groups.values())