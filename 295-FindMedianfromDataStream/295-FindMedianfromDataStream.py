# Last updated: 1/6/2026, 6:17:25 AM
1class MedianFinder:
2
3    def __init__(self):
4        self.small = []
5        self.large = []
6        
7
8    def addNum(self, num: int) -> None:
9        heapq.heappush(self.small,-num)
10        heapq.heappush(self.large,-heapq.heappop(self.small))
11
12        if len(self.small) < len(self.large):
13            heapq.heappush(self.small, -heapq.heappop(self.large))
14        
15
16    def findMedian(self) -> float:
17        if len(self.small) > len(self.large):
18            return -self.small[0]
19        else:
20            return (-self.small[0] + self.large[0])/2
21        
22
23
24# Your MedianFinder object will be instantiated and called as such:
25# obj = MedianFinder()
26# obj.addNum(num)
27# param_2 = obj.findMedian()