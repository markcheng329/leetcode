# Last updated: 1/11/2026, 3:52:57 AM
1class Solution:
2    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
3        seen = set()
4        
5        for t in triplets:
6            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
7                continue
8            
9            if t[0] == target[0]:
10                seen.add(0)
11            if t[1] == target[1]:
12                seen.add(1)
13            if t[2] == target[2]:
14                seen.add(2)
15        return True if len(seen) == 3 else False
16            