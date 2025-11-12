# Last updated: 11/12/2025, 4:57:22 AM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) < 3:
            return min(cost[0],cost[1])

        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[i],cost[i+1])

        