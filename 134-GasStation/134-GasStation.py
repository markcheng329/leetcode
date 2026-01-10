# Last updated: 1/9/2026, 10:13:12 PM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        if sum(gas) < sum(cost):
4            return -1
5        
6        total = 0
7        res = 0
8
9        for i in range(len(gas)):
10            total += gas[i]-cost[i]
11            if total < 0:
12                total = 0
13                res = i +1
14        return res