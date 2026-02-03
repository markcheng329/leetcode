# Last updated: 2/2/2026, 7:12:54 PM
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        l, r = 0,len(s)-1
4
5        while l < r:
6            if s[l] != s[r]:
7                if self.ispal(s,l+1,r) or self.ispal(s,l,r-1):
8                    return True
9                else:
10                    return False
11            else:
12                l +=1
13                r -=1
14        return True
15
16    
17
18
19
20    def ispal(self,s,l,r):
21        while l < r:
22            if s[l] != s[r]:
23                return False
24            else:
25                l +=1
26                r-=1
27        return True
28