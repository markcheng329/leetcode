# Last updated: 12/28/2025, 5:43:25 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        close_open = {")":"(","]":"[","}":"{"}
5
6        for i in range(len(s)):
7            if s[i] in close_open:
8                if stack and stack[-1] == close_open[s[i]]:
9                    stack.pop()
10                else:
11                    return False
12            else:
13                stack.append(s[i])
14        return True if not stack else False
15