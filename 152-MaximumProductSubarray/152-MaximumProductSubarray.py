# Last updated: 1/27/2026, 4:33:52 AM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        max_ans = min_ans = ans = nums[0]
4
5        for i in range(1,len(nums)):
6            if nums[i] < 0:
7                max_ans, min_ans = min_ans,max_ans
8
9            max_ans = max(nums[i],max_ans*nums[i])
10            min_ans = min(nums[i],min_ans*nums[i])
11
12            ans = max(ans,max_ans)
13        return ans