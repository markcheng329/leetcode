# Last updated: 12/28/2025, 6:15:27 AM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        res = [0] * len(temperatures)
4
5        stack = []
6
7        for i in range(len(temperatures)):
8            while stack and temperatures[stack[-1]] < temperatures[i]:
9                index = stack.pop()
10                res[index] = i-index
11            stack.append(i)
12        return res