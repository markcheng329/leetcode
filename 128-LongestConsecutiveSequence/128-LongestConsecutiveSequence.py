# Last updated: 12/11/2025, 1:54:56 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        numSet = set(nums)
4
5        res = 0
6
7        for num in numSet:
8            if num -1 not in numSet:
9                length = 1
10                while num + length in numSet:
11                    length +=1
12                res = max(res,length)
13        return res
14