# Last updated: 12/9/2025, 12:47:46 AM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        l, r = 0,len(arr)-k
4
5        while l < r:
6            mid = (l+r)//2
7
8            if x-arr[mid] > arr[mid+k]-x:
9                l = mid +1
10            else:
11                r = mid
12        return arr[l:l+k]