# Last updated: 1/2/2026, 4:25:00 AM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        stack = []
4
5        groups = sorted(zip(position,speed),reverse = True)
6
7        for position,speed in groups:
8            i = (target - position) / speed
9            while stack and i > stack[-1]:
10                stack.append(i)
11            stack.append(i) if stack == [] else None
12        return len(stack)