# Last updated: 1/10/2026, 2:29:52 AM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        a,b = nums1,nums2
4        if len(a) > len(b):
5            a,b = b,a
6        
7        m,n = len(a),len(b)
8
9        left = (m+n+1)//2
10
11        l, r = 0,m
12
13        while l <= r:
14            i = (l+r)//2
15            j = left -i
16
17            al = a[i-1] if i > 0 else float("-inf")
18            ar = a[i] if i < m else float("inf")
19            bl = b[j-1] if j > 0 else float("-inf")
20            br = b[j] if j < n else float("inf")
21
22            if al <= br and bl <= ar:
23                if (m+n) %2 ==1:
24                    return max(al,bl)
25                else:
26                    return float(max(al,bl) + min(ar,br)) /2.0
27            elif al > br:
28                r = i -1
29            else:
30                l = i +1