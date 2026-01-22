# Last updated: 1/22/2026, 5:38:14 AM
1class Solution:
2    def reverse(self, x: int) -> int:
3        intmax = 2**31-1
4        intmin = -2**31
5        min_div10 = int(intmin / 10) 
6
7
8        res = 0
9
10        while x!= 0:
11            digit = x % 10
12            if x < 0:
13                digit = -(abs(x) % 10)
14
15            x = int(x/10)
16
17            if res > intmax // 10 or (res == intmax//10 and digit > 7):
18                return 0
19            if res < int(intmin / 10)  or (res == int(intmin / 10)  and digit < -8):
20                return 0 
21            
22            res = res* 10 + digit
23        return res
24