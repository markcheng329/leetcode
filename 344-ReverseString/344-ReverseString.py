# Last updated: 2/2/2026, 1:48:25 PM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        l,r = 0,len(s)-1
7
8        while l < r:
9            s[l],s[r] = s[r],s[l]
10            l +=1
11            r -=1
12        
13        return s