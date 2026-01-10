# Last updated: 1/10/2026, 12:24:25 AM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        seen = set()
4
5        for num in nums:
6            if num in seen:
7                seen.remove(num)
8            else:
9                seen.add(num)
10        return list(seen)[0]