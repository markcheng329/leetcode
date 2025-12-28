# Last updated: 12/28/2025, 5:56:20 AM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack = []
4
5        for i in range(len(tokens)):
6            if tokens[i] not in ["+","-","*","/"]:
7                stack.append(int(tokens[i]))
8                continue
9
10            a = stack.pop()
11            b = stack.pop()
12            
13            if tokens[i] == "+":
14                stack.append(b+a)       
15            elif tokens[i] == "-":
16                stack.append(b-a)
17            elif tokens[i] == "*":
18                stack.append(b*a)
19            else:
20                stack.append(int(b/a))
21
22        return stack[-1]
23