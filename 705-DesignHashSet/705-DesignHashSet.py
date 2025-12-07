# Last updated: 12/7/2025, 12:08:54 AM
1class MyHashSet:
2
3    def __init__(self):
4        self.data = [False] * (10**6 +1)
5        
6
7    def add(self, key: int) -> None:
8        self.data[key] = True
9        
10
11    def remove(self, key: int) -> None:
12        self.data[key] = False
13        
14
15    def contains(self, key: int) -> bool:
16        return self.data[key]
17        
18
19
20# Your MyHashSet object will be instantiated and called as such:
21# obj = MyHashSet()
22# obj.add(key)
23# obj.remove(key)
24# param_3 = obj.contains(key)