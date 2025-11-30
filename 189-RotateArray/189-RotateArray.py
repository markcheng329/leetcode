# Last updated: 11/30/2025, 4:52:01 AM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        if len(nums) == 1:
7            return nums
8        k = k % len(nums)
9
10        self.reverse(nums,0,len(nums)-1)
11        self.reverse(nums,0,k-1)
12        self.reverse(nums,k,len(nums)-1)
13
14    def reverse(self,s,l,r):
15        while l < r:
16            s[l],s[r] = s[r],s[l]
17            l+=1 
18            r-=1
19        
20