# Last updated: 12/9/2025, 12:38:43 AM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        q = deque()
4        res = []
5        l = 0
6        i = 0
7
8        while i < len(nums):
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
21            i +=1
22        return res