# Last updated: 12/7/2025, 12:12:58 AM
1class MyHashMap:
2
3    def __init__(self):
4        self.map = [-1] * ( 10**6 +1)
5        
6
7    def put(self, key: int, value: int) -> None:
8        self.map[key] = value
9        
10    def get(self, key: int) -> int:
11        return self.map[key]
12        
13
14    def remove(self, key: int) -> None:
15        self.map[key] = -1
16        
17
18
19# Your MyHashMap object will be instantiated and called as such:
20# obj = MyHashMap()
21# obj.put(key,value)
22# param_2 = obj.get(key)
23# obj.remove(key)