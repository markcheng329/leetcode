# Last updated: 12/28/2025, 6:24:42 AM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        stack = []
4
5        groups = sorted(zip(position,speed), reverse = True)
6
7        for position, speed in groups:
8            i = (target - position) / (speed)
9            if not stack or stack[-1] < i:
10                stack.append(i)
11            else:
12                continue
13        return len(stack)