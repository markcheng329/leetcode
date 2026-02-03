# Last updated: 2/2/2026, 7:09:16 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        l,r = 0,len(s)-1
4
5        while l < r:
6            while l < r and not s[l].isalnum():
7                l +=1
8            while l < r and not s[r].isalnum():
9                r-=1
10            
11            if s[l].lower() != s[r].lower():
12                return False
13            else:
14                l +=1
15                r-=1
16        return True