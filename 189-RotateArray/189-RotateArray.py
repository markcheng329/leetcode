# Last updated: 11/30/2025, 4:53:35 AM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        if len(nums) == 1:
7            return nums
8            
9        k = k % len(nums)
10
11        self.reverse(nums,0,len(nums)-1)
12        self.reverse(nums,0,k-1)
13        self.reverse(nums,k,len(nums)-1)
14
15    def reverse(self,s,l,r):
16        while l < r:
17            s[l],s[r] = s[r],s[l]
18            l+=1 
19            r-=1
20        
21