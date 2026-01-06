# Last updated: 1/6/2026, 6:11:17 AM
1class MedianFinder:
2
3    def __init__(self):
4        self.small = []
5        self.large = []
6
7    def addNum(self, num: int) -> None:
8        heapq.heappush(self.small,-num)
9        heapq.heappush(self.large,-heapq.heappop(self.small))
10
11        if len(self.small ) < len(self.large):
12            heapq.heappush(self.small, -heapq.heappop(self.large))
13        
14
15    def findMedian(self) -> float:
16        if len(self.small) > len(self.large):
17            return -self.small[0]
18        else:
19            return (-self.small[0] + self.large[0])/2
20        
21
22
23# Your MedianFinder object will be instantiated and called as such:
24# obj = MedianFinder()
25# obj.addNum(num)
26# param_2 = obj.findMedian()