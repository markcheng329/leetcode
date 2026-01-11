# Last updated: 1/11/2026, 4:23:52 AM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        a,b = nums1,nums2
4        if len(a) > len(b):
5            a,b = b,a
6        m = len(a)
7        n = len(b)
8        left = (m+n+1)//2
9        l,r = 0,m
10
11        while l <=r :
12            i = (l+r)//2
13            j = left -i
14            
15            al = a[i-1] if i > 0 else float("-inf")
16            ar = a[i] if i < m else float("inf")
17            bl = b[j-1] if j > 0 else float("-inf")
18            br = b[j] if j < n else float("inf")
19
20            if al <= br and bl <= ar:
21                if (m+n) %2 == 1:
22                    return max(al,bl)
23                else:
24                    return float(max(al,bl) + min(ar,br))/2.0
25            elif al> br:
26                r = i-1
27            else:
28                l = i +1