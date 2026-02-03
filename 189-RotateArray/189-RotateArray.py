# Last updated: 2/2/2026, 7:57:37 PM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6
7        if len(nums) <= 1:
8            return nums
9
10        k = k % len(nums)
11        self.rotateall(nums,0,len(nums)-1)
12        self.rotateall(nums,0,k-1)
13        self.rotateall(nums,k,len(nums)-1)
14
15    
16
17
18    def rotateall(self,nums,l,r):
19        while l < r:
20            nums[l],nums[r] = nums[r],nums[l]
21            l +=1
22            r -=1
23        