# Last updated: 12/30/2025, 9:31:03 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        l ,r = 0, len(matrix) * len(matrix[0]) -1
4
5        while l <= r:
6            mid = (l+r)//2
7            row = mid // len(matrix[0])
8            col = mid % len(matrix[0])
9            val = matrix[row][col]
10
11            if val > target:
12                r = mid-1
13            elif val < target:
14                l = mid+1
15            else:
16                return True
17        return False
18