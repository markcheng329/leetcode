# Last updated: 1/31/2026, 12:34:22 AM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        cand1,cand2 = None,None
4        count1,count2 = 0,0
5
6        for num in nums:
7            if num == cand1:
8                count1 +=1
9            elif num == cand2:
10                count2 +=1
11            elif count1 == 0:
12                cand1,count1 = num,1
13            elif count2 == 0:
14                cand2,count2 = num,1
15            else:
16                count1 -=1
17                count2 -=1
18        
19        res = []
20        n = len(nums)
21        count1,count2 = 0,0
22        for num in nums:
23            if num == cand1:
24                count1 +=1
25            elif num == cand2:
26                count2 +=1
27        
28        if count1 > n//3:
29            res.append(cand1)
30        if count2 > n//3:
31            res.append(cand2)
32        
33        return res