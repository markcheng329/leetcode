# Last updated: 1/20/2026, 3:25:35 AM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        
4        if len(cost) < 3:
5            return min(cost[0],cost[1])
6
7        for i in range(len(cost)-3,-1,-1):
8            cost[i] += min(cost[i+1],cost[i+2])
9        return min(cost[0],cost[1])