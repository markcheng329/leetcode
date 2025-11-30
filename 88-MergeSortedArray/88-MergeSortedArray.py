# Last updated: 11/30/2025, 2:03:47 AM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        last = m + n -1
7
8        while m > 0 and n > 0:
9            if nums1[m-1] > nums2[n-1]:
10                nums1[last] = nums1[m-1]
11                m-=1
12            else:
13                nums1[last] = nums2[n-1]
14                n-=1
15
16            last -=1
17        
18        while n > 0:
19            nums1[last] = nums2[n-1]
20            last -=1
21            n-=1
22        
23        return nums1