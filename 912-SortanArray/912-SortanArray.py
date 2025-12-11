# Last updated: 12/10/2025, 11:53:18 PM
1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        if len (nums) <= 1:
4            return nums
5        
6        mid = (len(nums)) //2
7
8        left = self.sortArray(nums[:mid])
9        right = self.sortArray(nums[mid:])
10    
11        return self.merge(left,right)
12
13    def merge(self,left,right):
14        i = j = 0
15        res = []
16
17        while i < len(left) and j < len(right):
18            if left[i] < right[j]:
19                res.append(left[i])
20                i +=1
21            else:
22                res.append(right[j])
23                j +=1
24        
25        while i < len(left):
26            res.append(left[i])
27            i +=1
28
29        while j < len(right):
30            res.append(right[j])
31            j +=1
32
33        return res
34
35