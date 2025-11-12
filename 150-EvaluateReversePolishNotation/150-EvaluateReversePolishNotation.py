# Last updated: 11/12/2025, 4:58:49 AM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in {"+","-","*","/"}:
                stack.append(int(i))
                continue
        
            a = stack.pop()
            b = stack.pop()


            if i == "+":
                stack.append(b+a)
            elif i == "-":
                stack.append(b-a)
            elif i == "*":
                stack.append(b*a)
            else:
                stack.append(int(b/a))

        return stack[-1]
            

        
