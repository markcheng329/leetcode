# Last updated: 1/2/2026, 4:37:11 AM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        m = len(matrix)
4        n = len(matrix[0])
5        l,r = 0,m*n-1
6
7        while l <= r:
8            mid = (l+r)//2
9            row = mid // n
10            col = mid % n
11
12            if matrix[row][col] == target:
13                return True
14            
15            if matrix[row][col] > target:
16                r = mid -1
17            else:
18                l = mid +1
19        return False