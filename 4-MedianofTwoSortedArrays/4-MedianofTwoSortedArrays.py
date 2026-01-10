# Last updated: 1/10/2026, 1:08:10 AM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        merge = nums1 +nums2
4        merge.sort()
5
6        totallen = len(merge)
7        if totallen %2 == 0:
8            return ((merge[totallen//2-1]) + (merge[totallen//2]) )/2.0
9        else:
10            return merge[totallen//2]