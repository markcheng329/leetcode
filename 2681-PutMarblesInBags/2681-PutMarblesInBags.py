# Last updated: 11/12/2025, 4:56:51 AM
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        pair_cost = [weights[i]+weights[i+1] for i in range(len(weights)-1)]

        pair_cost.sort()

        max_cost = sum(pair_cost[-(k-1):])

        min_cost = sum(pair_cost[:(k-1)])

        res = max_cost - min_cost

        return res