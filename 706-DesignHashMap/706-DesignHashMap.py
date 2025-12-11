# Last updated: 12/10/2025, 11:23:32 PM
1class MyHashMap:
2
3    def __init__(self):
4        self.map = [-1] * (10**6+1)
5        
6
7    def put(self, key: int, value: int) -> None:
8        self.map[key] = value
9        
10
11    def get(self, key: int) -> int:
12        return self.map[key]
13        
14
15    def remove(self, key: int) -> None:
16        self.map[key] = -1
17        
18
19
20# Your MyHashMap object will be instantiated and called as such:
21# obj = MyHashMap()
22# obj.put(key,value)
23# param_2 = obj.get(key)
24# obj.remove(key)