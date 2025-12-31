# Last updated: 12/31/2025, 4:02:26 AM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        l,r = 1,max(piles)
4        res = r
5
6        while l <= r:
7            mid = (l+r)//2
8            hours = sum(math.ceil(p/mid) for p in piles)
9            if hours <= h:
10                res = min(res,mid)
11                r = mid -1
12            else:
13                l = mid +1
14        return res