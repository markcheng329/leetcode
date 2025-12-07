# Last updated: 12/6/2025, 10:32:12 PM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        res = ""
4
5        for i in range(len(strs[0])):
6            for s in strs:
7                if i == len(s) or s[i] != strs[0][i]:
8                    return res
9            res += strs[0][i]
10        return res
11