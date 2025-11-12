# Last updated: 11/12/2025, 4:57:17 AM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        groups = sorted(zip(position,speed),reverse = True)

        for position,speed in groups:
            i = (target - position)/(speed)
            if not stack or stack[-1] < i:
                stack.append(i)
            else:
                continue
        return len(stack)

