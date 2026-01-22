# Last updated: 1/22/2026, 3:29:15 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = set()
4        res = 0
5        l = 0
6
7        for i in range(len(s)):
8            while s[i] in seen:
9                seen.remove(s[l])
10                l +=1
11            seen.add(s[i])
12            res = max(res,i-l+1)
13        return res