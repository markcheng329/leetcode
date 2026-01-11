# Last updated: 1/11/2026, 4:17:45 AM
1class TimeMap:
2
3    def __init__(self):
4        self.keystore = {}
5        
6
7    def set(self, key: str, value: str, timestamp: int) -> None:
8        if key not in self.keystore:
9            self.keystore[key]= []
10        self.keystore[key].append([value,timestamp])
11        
12
13    def get(self, key: str, timestamp: int) -> str:
14        values = self.keystore.get(key,[])
15        res = ""
16        l, r = 0,len(values)-1
17        while l <= r:
18            mid = (l+r)//2
19            if values[mid][1]  <= timestamp:
20                res = values[mid][0]
21                l = mid +1
22            else:
23                r = mid -1
24        return res
25
26        
27        
28
29
30# Your TimeMap object will be instantiated and called as such:
31# obj = TimeMap()
32# obj.set(key,value,timestamp)
33# param_2 = obj.get(key,timestamp)