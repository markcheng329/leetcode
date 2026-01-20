# Last updated: 1/20/2026, 3:08:33 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        cur,prev = 1,1
4        for i in range(n-1):
5            temp = cur
6            cur = cur+prev
7            prev = temp
8        return cur