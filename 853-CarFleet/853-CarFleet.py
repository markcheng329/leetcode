# Last updated: 1/2/2026, 4:27:29 AM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        stack = []
4
5        groups = sorted(zip(position,speed),reverse = True)
6
7        for pos,spe in groups:
8            i = (target - pos) / spe
9            if not stack or i > stack[-1]:
10                stack.append(i)
11        return len(stack)