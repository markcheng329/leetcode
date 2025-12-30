# Last updated: 12/30/2025, 6:08:48 PM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        q = deque()
4        l = 0
5        res = []
6        i = 0
7
8        while i < len(nums):
9            while q and nums[q[-1]] < nums[i]:
10                q.pop()
11
12            q.append(i)
13
14
15
16            if i-l+1 == k:
17                res.append(nums[q[0]])
18                l +=1
19            
20            while q and q[0] < l:
21                q.popleft()
22            
23            i +=1
24            
25        return res