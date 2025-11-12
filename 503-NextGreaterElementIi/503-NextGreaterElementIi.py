# Last updated: 11/12/2025, 4:57:36 AM
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1]*n

        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                res[stack.pop()] = nums[i%n]
            if i < n:
                stack.append(i)
        return res