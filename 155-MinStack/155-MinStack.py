# Last updated: 1/2/2026, 3:50:34 AM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.minstack = []
6        
7
8    def push(self, val: int) -> None:
9        self.stack.append(val)
10        val = min(val,self.minstack[-1]) if self.minstack else val
11        self.minstack.append(val)
12
13    def pop(self) -> None:
14        self.stack.pop()
15        self.minstack.pop()
16        
17
18    def top(self) -> int:
19        return self.stack[-1]
20        
21
22    def getMin(self) -> int:
23        return self.minstack[-1]
24
25
26# Your MinStack object will be instantiated and called as such:
27# obj = MinStack()
28# obj.push(val)
29# obj.pop()
30# param_3 = obj.top()
31# param_4 = obj.getMin()