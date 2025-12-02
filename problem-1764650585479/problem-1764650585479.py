# Last updated: 12/1/2025, 11:43:05 PM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3
4        """
5        Do not return anything, modify nums in-place instead.
6        """
7
8        if len(nums) <= 1:
9            return nums
10        
11        k = k % len(nums)
12        self.reverse(nums,0,len(nums)-1)
13        self.reverse(nums,0,k-1)
14        self.reverse(nums,k,len(nums)-1)
15        
16    def reverse(self,nums,l,r):
17        while l < r:
18            nums[l],nums[r] = nums[r],nums[l]
19            l +=1
20            r-=1
21        
22