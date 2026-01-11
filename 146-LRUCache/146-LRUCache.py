# Last updated: 1/11/2026, 6:07:34 AM
1class Node:
2    def __init__(self,key,value):
3        self.key = key
4        self.value = value
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
15    def add(self,node):
16        prev,nxt = self.right.prev,self.right
17        prev.next = nxt.prev = node
18        node.prev,node.next = prev,nxt
19    
20    def remove(self,node):
21        prev,nxt = node.prev,node.next
22        prev.next, nxt.prev = nxt,prev
23        
24    def get(self, key: int) -> int:
25        if key in self.cache:
26            self.remove(self.cache[key])
27            self.add(self.cache[key])
28            return self.cache[key].value
29        return -1
30        
31
32    def put(self, key: int, value: int) -> None:
33        if key in self.cache:
34            self.remove(self.cache[key])
35        self.cache[key] = Node(key,value)
36        self.add(self.cache[key])
37
38        if len(self.cache) > self.cap:
39            lru = self.left.next
40            self.remove(lru)
41            del self.cache[lru.key]
42        
43
44
45# Your LRUCache object will be instantiated and called as such:
46# obj = LRUCache(capacity)
47# param_1 = obj.get(key)
48# obj.put(key,value)