# Last updated: 11/12/2025, 4:57:16 AM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l+r)//2
            hours = sum(math.ceil(p/mid) for p in piles)

            if hours<=h:
                res = min(res,mid)
                r = mid-1
            else:
                l = mid +1
        return res