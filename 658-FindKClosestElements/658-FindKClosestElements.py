# Last updated: 12/6/2025, 9:46:42 PM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        l , r = 0,len(arr)-1
4
5        while r-l+1>k:
6            if abs(arr[l]-x) > abs(arr[r]-x):
7                l +=1
8            else:
9                r-=1
10        return arr[l:r+1]