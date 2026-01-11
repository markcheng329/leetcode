# Last updated: 1/11/2026, 3:42:58 AM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        if sum(gas) < sum(cost):
4            return -1
5        
6        total = 0
7        res = 0
8        for i in range(len(gas)):
9            total += gas[i] - cost[i]
10            if total < 0:
11                total = 0
12                res = i+1
13        return res
14