# Last updated: 12/18/2025, 1:43:41 AM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        q = deque()
4        l = 0
5        res = []
6
7
8        for i in range(len(nums)):
9            while q and nums[q[-1]] < nums[i]:
10                q.pop()
11
12            q.append(i)
13
14            if l > q[0]:
15                q.popleft()
16            
17            if i-l+1 == k:
18                res.append(nums[q[0]])
19                l +=1
20        
21
22        return res
23