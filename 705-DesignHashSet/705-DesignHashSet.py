# Last updated: 12/10/2025, 11:03:51 PM
1class MyHashSet:
2
3    def __init__(self):
4        self.data = [False] * (10**6+1)    
5
6    def add(self, key: int) -> None:
7        self.data[key] = True
8
9        
10    def remove(self, key: int) -> None:
11        self.data[key] = False
12        
13
14    def contains(self, key: int) -> bool:
15        return self.data[key]
16        
17
18
19# Your MyHashSet object will be instantiated and called as such:
20# obj = MyHashSet()
21# obj.add(key)
22# obj.remove(key)
23# param_3 = obj.contains(key)