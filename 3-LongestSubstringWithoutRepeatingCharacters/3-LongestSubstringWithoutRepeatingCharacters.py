# Last updated: 12/3/2025, 8:58:31 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = set()
4
5        res = 0
6        l = 0
7
8        for i in range(len(s)):
9            while s[i] in seen:
10                seen.remove(s[l])
11                l +=1
12            seen.add(s[i])
13            res = max(res,i-l+1)
14        return res
15        