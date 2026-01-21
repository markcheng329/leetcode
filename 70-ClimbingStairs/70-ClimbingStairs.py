# Last updated: 1/21/2026, 5:02:47 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        cur,prev = 1,1
4
5        for i in range(n-1):
6            temp = cur
7            cur = cur+ prev
8            prev = temp
9        return cur