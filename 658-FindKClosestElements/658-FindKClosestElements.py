# Last updated: 12/2/2025, 2:54:24 AM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        l, r = 0, len(arr) - k
4        while l < r:
5            m = (l + r) // 2
6            if x - arr[m] > arr[m + k] - x:
7                l = m + 1
8            else:
9                r = m
10        return arr[l:l + k]