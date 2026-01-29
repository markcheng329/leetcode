# Last updated: 1/28/2026, 11:30:52 PM
1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        if len(nums) <= 1:
4            return nums
5        
6        mid = (len(nums))//2
7
8        left = self.sortArray(nums[:mid])
9        right = self.sortArray(nums[mid:])
10
11        return self.merge(left,right)
12    
13
14    def merge(self,left,right):
15        i,j = 0,0
16        res = []
17
18        while i < len(left) and j < len(right):
19            if left[i] <= right[j]:
20                res.append(left[i])
21                i +=1
22            else:
23                res.append(right[j])
24                j +=1
25
26        while i < len(left):
27            res.append(left[i])
28            i +=1
29        
30        while j < len(right):
31            res.append(right[j])
32            j +=1
33        return res
34