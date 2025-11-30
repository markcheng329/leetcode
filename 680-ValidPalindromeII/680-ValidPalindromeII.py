# Last updated: 11/30/2025, 1:47:46 AM
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        l,r = 0,len(s)-1
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
16    def ispal(self,s,l,r):
17        while l < r:
18            if s[l] != s[r]:
19                return False
20            else:
21                l +=1
22                r-=1
23        return True