# Last updated: 1/10/2026, 2:20:41 AM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        a,b = nums1,nums2
4        if len(a) > len(b):
5            b,a = a,b
6        
7        m,n = len(a),len(b)
8
9        left = (m+n+1)//2
10        l,r = 0,m
11
12        while l <= r:
13            i = (l+r)//2
14            j = left -i
15            
16            al = a[i-1] if i > 0 else float("-inf")
17            ar = a[i] if i < m else float("inf")
18            bl = b[j-1] if j > 0 else float("-inf")
19            br = b[j] if j < n else float("inf")
20
21            if al <= br and bl <= ar:
22                if (m+n) % 2== 1:
23                    return max(al,bl)
24                else:
25                    return float(max(al,bl) + min(ar,br))/2.0
26            elif al > br:
27                r = i-1
28            else:
29                l = i +1