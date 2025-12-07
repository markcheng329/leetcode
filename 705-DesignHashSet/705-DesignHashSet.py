# Last updated: 12/7/2025, 12:10:00 AM
1class MyHashSet:
2
3    def __init__(self):
4        self.data = []
5        
6
7    def add(self, key: int) -> None:
8        if key not in self.data:
9            self.data.append(key)
10        
11
12    def remove(self, key: int) -> None:
13        if key in self.data:
14            self.data.remove(key)
15        
16
17    def contains(self, key: int) -> bool:
18        return key in self.data
19        
20
21
22# Your MyHashSet object will be instantiated and called as such:
23# obj = MyHashSet()
24# obj.add(key)
25# obj.remove(key)
26# param_3 = obj.contains(key)