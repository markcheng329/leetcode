# Last updated: 1/22/2026, 5:41:49 AM
1class Solution:
2    def reverse(self, x: int) -> int:
3        intmax = 2**31-1
4        intmin = -2**31
5
6        res = 0
7
8        while x!= 0:
9            digit = x % 10
10            if x < 0:
11                digit = -(abs(x) % 10)
12            
13            x = int(x/10)
14
15            if res > intmax//10 or (res == intmax//10 and digit > 7):
16                return 0
17            
18            if res < int(intmin/10) or (res == int(intmin/10) and digit < -8):
19                return 0
20            
21            res = res*10 + digit
22        return res