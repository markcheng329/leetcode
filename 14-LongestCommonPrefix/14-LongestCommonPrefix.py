# Last updated: 12/10/2025, 9:18:03 PM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        res = []
4
5        for i in range(len(strs[0])):
6            for s in strs:
7                if i == len(s) or strs[0][i] != s[i]:
8                    return "".join(res)
9            res.append(strs[0][i])
10        return "".join(res)