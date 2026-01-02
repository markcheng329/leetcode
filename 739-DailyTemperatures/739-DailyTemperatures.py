# Last updated: 1/2/2026, 4:02:39 AM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        stack = []
4        res = [0] * len(temperatures)
5
6        for i in range(len(temperatures)):
7            while stack and stack[-1][1] < temperatures[i]:
8                index,temp = stack.pop()
9                res[index] = i -index
10            stack.append([i,temperatures[i]])
11        return res