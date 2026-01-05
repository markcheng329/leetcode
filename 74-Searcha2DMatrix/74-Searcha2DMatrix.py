# Last updated: 1/4/2026, 8:57:25 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        m = len(matrix)
4        n = len(matrix[0])
5
6        l,r = 0,m*n-1
7
8        while l <= r:
9            mid = (l+r)//2
10            row = mid //n
11            col = mid % n
12            if matrix[row][col] == target:
13                return True
14            
15            if matrix[row][col] > target:
16                r = mid -1
17            else:
18                l = mid +1
19        return False