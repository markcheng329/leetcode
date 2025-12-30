# Last updated: 12/30/2025, 6:42:23 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        
4        stack = []
5
6        groups = sorted(zip(position,speed), reverse = True)
7
8        for position, speed in groups:
9            i = (target-position) /speed
10            if not stack or stack[-1] < i:
11                stack.append(i)
12            else:
13                continue
14        return len(stack)
15        