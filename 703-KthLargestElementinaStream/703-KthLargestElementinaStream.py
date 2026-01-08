# Last updated: 1/7/2026, 7:24:23 PM
1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        self.minheap = nums
5        self.k = k
6        heapq.heapify(self.minheap)
7        
8
9    def add(self, val: int) -> int:
10        heapq.heappush(self.minheap,val)
11        while len(self.minheap) > self.k:
12            heapq.heappop(self.minheap)
13        return self.minheap[0]
14        
15
16
17# Your KthLargest object will be instantiated and called as such:
18# obj = KthLargest(k, nums)
19# param_1 = obj.add(val)