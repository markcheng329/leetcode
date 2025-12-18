# Last updated: 12/17/2025, 10:20:31 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        freq = [[]for i in range(len(nums)+1)]
4
5        count = Counter(nums)
6        res = []
7
8        for num, c in count.items():
9            freq[c].append(num)
10        
11        for i in range(len(freq)-1,-1,-1):
12            for num in freq[i]:
13                res.append(num)
14                if len(res) == k:
15                    return res
16
17