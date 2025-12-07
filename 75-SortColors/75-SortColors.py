# Last updated: 12/7/2025, 12:59:39 AM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        left,right = 0 ,len(nums)-1
7        
8        i = 0
9
10        while i <= right:
11            if nums[i] == 0:
12                nums[i],nums[left] = nums[left],nums[i]
13                i +=1
14                left +=1
15            elif nums[i] == 2:
16                nums[i],nums[right] = nums[right],nums[i]
17                right -=1
18            else:
19                i +=1
20