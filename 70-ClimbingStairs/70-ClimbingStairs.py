# Last updated: 1/20/2026, 3:07:31 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        one,two = 1,1
4        for i in range(n-1):
5            temp = one
6            one = one + two
7            two = temp
8        return one