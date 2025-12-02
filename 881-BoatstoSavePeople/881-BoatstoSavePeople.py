# Last updated: 12/2/2025, 12:26:41 AM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        l, r = 0,len(people)-1
5        res = 0
6
7
8        while l <= r:
9            if people[l] + people[r] <= limit:
10                l +=1
11                r-=1
12                res +=1
13            else:
14                r-=1
15                res +=1
16        return res