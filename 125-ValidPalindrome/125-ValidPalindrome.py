# Last updated: 12/17/2025, 11:42:24 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        l, r = 0,len(s)-1
4
5        while l < r:
6            while l < r and not s[l].isalnum():
7                l +=1
8                
9            while l < r and not s[r].isalnum():
10                r-=1
11            
12            if s[l].lower() != s[r].lower():
13                return False
14            else:
15                l +=1
16                r-=1
17        return True
18