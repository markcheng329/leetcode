# Last updated: 12/30/2025, 6:36:57 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        stack = []
4        res = [0] * len(temperatures)
5
6        for i in range(len(temperatures)):
7            while stack and temperatures[stack[-1]] < temperatures[i]:
8                index = stack.pop()
9                res[index] = i-index
10
11            stack.append(i)
12        return res