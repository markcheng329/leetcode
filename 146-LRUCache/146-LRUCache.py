# Last updated: 1/21/2026, 5:27:11 AM
1class Node:
2
3    def __init__(self,key,value):
4        self.key,self.value = key,value
5        self.prev = self.next = None
6
7class LRUCache:
8
9    def __init__(self, capacity: int):
10        self.cap = capacity
11        self.cache = {}
12        self.left,self.right = Node(0,0),Node(0,0)
13        self.left.next,self.right.prev = self.right,self.left
14    
15    def remove(self,node):
16        prev,nxt = node.prev,node.next
17        prev.next,nxt.prev = nxt,prev
18    
19    def add(self,node):
20        prev,nxt = self.right.prev,self.right
21        prev.next = nxt.prev = node
22        node.prev,node.next = prev,nxt
23        
24
25    def get(self, key: int) -> int:
26        if key in self.cache:
27            self.remove(self.cache[key])
28            self.add(self.cache[key])
29            return self.cache[key].value
30        return -1
31        
32
33    def put(self, key: int, value: int) -> None:
34        if key in self.cache:
35            self.remove(self.cache[key])
36        self.cache[key] = Node(key,value)
37        self.add(self.cache[key])
38
39        if len(self.cache) > self.cap:
40            lru = self.left.next
41            self.remove(lru)
42            del self.cache[lru.key]
43        
44
45
46# Your LRUCache object will be instantiated and called as such:
47# obj = LRUCache(capacity)
48# param_1 = obj.get(key)
49# obj.put(key,value)