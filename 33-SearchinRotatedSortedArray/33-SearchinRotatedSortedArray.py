# Last updated: 12/31/2025, 3:38:09 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0 , len(nums)-1
4
5        while l <= r:
6            mid = (l+r)//2
7
8            if nums[mid] == target:
9                return mid
10
11            if nums[l] <= nums[mid]:
12                if nums[mid] > target >= nums[l]:
13                    r = mid -1
14                else:
15                    l = mid +1
16            else:
17                # nums[r] > nums[mid]
18                if nums[r] >= target > nums[mid]:
19                    l = mid +1 
20                else:
21                    r = mid -1
22        return -1