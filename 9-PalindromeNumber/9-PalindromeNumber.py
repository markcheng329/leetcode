# Last updated: 1/22/2026, 5:45:34 AM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x < 0:
4            return False
5
6        if x > 0 and x % 10 == 0:
7            return False
8
9        rev = 0
10        while x > rev:
11            rev = rev * 10 + x % 10
12            x //= 10
13
14        return x == rev or x == rev // 10