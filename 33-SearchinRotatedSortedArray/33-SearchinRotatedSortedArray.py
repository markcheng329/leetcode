# Last updated: 1/2/2026, 5:23:10 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0,len(nums)-1
4
5        while l <= r:
6            mid = (l+r)//2
7            if nums[mid] == target:
8                return mid
9
10            if nums[mid] < nums[r]:
11                if nums[r]>= target >nums[mid]:
12                    l = mid +1
13                else:
14                    r = mid -1
15            else:
16                if nums[l] <= target < nums[mid]:
17                    r = mid -1
18                else:
19                    l = mid +1
20        return -1
21