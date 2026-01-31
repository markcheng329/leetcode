# Last updated: 1/31/2026, 12:42:46 AM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        cand1,cand2 = None,None
4        count1,count2 = 0,0
5        n = len(nums)
6
7        for i in range(len(nums)):
8            if nums[i] == cand1:
9                count1 +=1
10            elif nums[i] == cand2:
11                count2 +=1
12            elif count1 == 0:
13                cand1, count1 = nums[i], 1
14            elif count2 == 0:
15                cand2,count2 = nums[i], 1
16            else:
17                count1 -=1
18                count2 -=1
19        
20        res = []
21        count1,count2 = 0,0
22        for i in range(len(nums)):
23            if nums[i] == cand1:
24                count1 +=1
25            elif nums[i] == cand2:
26                count2 +=1
27        
28        if count1 > n//3:
29            res.append(cand1)
30        if count2 > n//3:
31            res.append(cand2)
32
33        return res