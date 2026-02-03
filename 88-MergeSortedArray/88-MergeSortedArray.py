# Last updated: 2/2/2026, 7:46:27 PM
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
11                m -=1
12            else:
13                nums1[last] = nums2[n-1]
14                n-=1
15            last -=1
16        
17        while m > 0:
18            nums1[last] = nums1[m-1]
19            m-=1
20            last -=1
21        
22        while n > 0:
23            nums1[last] = nums2[n-1]
24            n-=1
25            last -=1
26