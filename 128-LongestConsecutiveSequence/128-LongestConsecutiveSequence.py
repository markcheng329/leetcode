# Last updated: 12/17/2025, 11:15:10 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        numsSet = set(nums)
4        res = 0
5
6        for num in numsSet:
7            if num -1 not in numsSet:
8                length = 1
9                while num + length in numsSet:
10                    length +=1
11                res = max(res,length)
12        return res
13        