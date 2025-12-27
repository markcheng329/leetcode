# Last updated: 12/27/2025, 12:57:15 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l, r = 0,len(numbers)-1
4
5        while l < r:
6            if numbers[l] + numbers[r] > target:
7                r-=1
8            elif numbers[l] + numbers[r] < target:
9                l +=1
10            else:
11                return [l+1,r+1]