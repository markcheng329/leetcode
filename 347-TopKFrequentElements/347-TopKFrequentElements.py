# Last updated: 12/11/2025, 1:24:12 AM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        freq = [[] for i in range(len(nums)+1)]
4        res = []
5        count = Counter(nums)
6
7        for num,c in count.items():
8            freq[c].append(num)
9        
10        for i in range(len(freq)-1,-1,-1):
11            for num in freq[i]:
12                res.append(num)
13                if len(res) == k:
14                    return res
15
16