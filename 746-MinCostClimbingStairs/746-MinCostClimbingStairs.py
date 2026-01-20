# Last updated: 1/20/2026, 3:29:05 AM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        if len(cost) < 3:
4            return min(cost[0],cost[1])
5        
6        for i in range(len(cost)-3,-1,-1):
7            cost[i] += min(cost[i+1],cost[i+2])
8        return min(cost[0],cost[1])