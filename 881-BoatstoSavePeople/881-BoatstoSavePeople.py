# Last updated: 11/30/2025, 5:08:26 AM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        l, r = 0,len(people)-1
5        res = 0
6
7        while l <= r:
8            if people[l] + people[r] <= limit:
9                l +=1
10            r -=1
11            res +=1
12        return res