# Last updated: 11/30/2025, 1:43:01 AM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        l, r = 0, len(s)-1
7
8        while l < r:
9            s[l],s[r] = s[r],s[l]
10            l +=1
11            r-=1
12        