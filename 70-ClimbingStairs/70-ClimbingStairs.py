# Last updated: 11/13/2025, 4:27:02 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1,1
        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
        return one