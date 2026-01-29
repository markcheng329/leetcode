# Last updated: 1/28/2026, 11:11:38 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        l,r = 0,len(nums)-1
7        i = 0
8
9        while i <= r:
10            if nums[i] == 0:
11                nums[l],nums[i] = nums[i],nums[l]
12                i +=1
13                l +=1
14            elif nums[i] == 2:
15                nums[r],nums[i] = nums[i],nums[r]
16                r-=1
17            else:
18                i +=1
19        return nums