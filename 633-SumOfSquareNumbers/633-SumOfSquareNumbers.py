# Last updated: 11/12/2025, 4:57:32 AM
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.isqrt(c))

        while left <= right:
            total = left*left + right*right
            if total > c:
                right -=1
            elif total < c:
                left +=1
            else:
                return True
        return False