# Last updated: 12/18/2025, 12:28:39 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        l = 0
4        seen = set()
5        res = 0
6
7        for i in range(len(s)):
8            while s[i] in seen:
9                seen.remove(s[l])
10                l +=1
11            else:
12                seen.add(s[i])
13            res = max(res,i-l+1)
14        return res