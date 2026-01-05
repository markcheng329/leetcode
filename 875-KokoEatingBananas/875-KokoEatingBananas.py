# Last updated: 1/4/2026, 9:02:26 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        l, r = 1,max(piles)
4
5        res = r
6
7        while l <= r:
8            mid = (l+r)//2
9            hours = sum(math.ceil(p/mid) for p in piles)
10
11            if hours <= h:
12                res = min(res,mid)
13                r = mid -1
14            else:
15                l = mid +1
16
17        return res