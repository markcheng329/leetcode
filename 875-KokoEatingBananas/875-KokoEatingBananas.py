# Last updated: 1/2/2026, 4:40:36 AM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        l, r = 1, max(piles)
4        res = r
5
6        while l <= r:
7            mid = (l+r)//2
8            hours = sum(math.ceil(p/mid) for p in piles)
9
10            if hours<= h:
11                res = min(res,mid)
12                r = mid -1
13            else:
14                l = mid +1
15        return res