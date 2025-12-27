# Last updated: 12/27/2025, 2:38:30 AM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        i = 0
4        l = 0
5        res = []
6        q = deque()
7
8        while i < len(nums):
9            #q=[0,-1]
10            while q and nums[q[-1]] < nums[i]:
11                q.pop()
12            
13            q.append(i)
14
15            if l > q[0]:
16                q.popleft()
17            
18            if i-l+1 == k:
19                res.append(nums[q[0]])
20                l +=1
21            i+=1
22        return res