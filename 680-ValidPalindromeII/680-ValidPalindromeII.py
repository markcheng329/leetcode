# Last updated: 11/29/2025, 1:17:32 AM
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        l , r = 0,len(s)-1
4        while l < r:
5            if s[l] == s[r]:
6                l +=1
7                r-=1
8            else:
9                if self.ispal(s,l+1,r) or self.ispal(s,l,r-1):
10                    return True
11                else:
12                    return False
13        return True
14    
15
16
17    def ispal(self,s,l,r):
18        while l < r:
19            if s[l] != s[r]:
20                return False
21            else:
22                l +=1
23                r -=1
24        return True