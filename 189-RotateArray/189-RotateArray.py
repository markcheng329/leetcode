# Last updated: 2/2/2026, 7:59:11 PM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6
7        if len(nums) <= 1:
8            return
9
10        k = k % len(nums)
11        if k == 0:
12            return
13            
14        self.rotateall(nums,0,len(nums)-1)
15        self.rotateall(nums,0,k-1)
16        self.rotateall(nums,k,len(nums)-1)
17
18    
19
20
21    def rotateall(self,nums,l,r):
22        while l < r:
23            nums[l],nums[r] = nums[r],nums[l]
24            l +=1
25            r -=1
26        