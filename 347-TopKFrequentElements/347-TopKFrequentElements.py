# Last updated: 11/18/2025, 9:02:09 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = Counter(nums)
        for num, c in count.items():
            freq[c].append(num)
        res = []
        
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                k -=1
                if k == 0:
                    return res
