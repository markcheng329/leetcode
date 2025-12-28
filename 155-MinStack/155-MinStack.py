# Last updated: 12/28/2025, 5:50:24 AM
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
13
14    def pop(self) -> None:
15        self.stack.pop()
16        self.minstack.pop()
17        
18
19    def top(self) -> int:
20        return self.stack[-1]
21        
22
23    def getMin(self) -> int:
24        return self.minstack[-1]
25        
26
27
28# Your MinStack object will be instantiated and called as such:
29# obj = MinStack()
30# obj.push(val)
31# obj.pop()
32# param_3 = obj.top()
33# param_4 = obj.getMin()