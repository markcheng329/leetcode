# Last updated: 12/11/2025, 2:01:23 AM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        count = Counter(nums)
4
5        res = []
6
7        for key in count:
8            if count[key] > len(nums) //3:
9                res.append(key)
10        return res