# Last updated: 1/28/2026, 7:18:10 PM
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        l, r = 0, len(matrix)-1
7
8        while l < r:
9            for i in range(r-l):
10                topleft = matrix[l][l+i]
11                matrix[l][l+i] = matrix[r-i][l]
12                matrix[r-i][l] = matrix[r][r-i]
13                matrix[r][r-i] = matrix[l+i][r]
14                matrix[l+i][r] = topleft
15            
16            l+=1
17            r-=1