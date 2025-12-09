# Last updated: 12/9/2025, 1:18:20 AM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        res = 0
4        people.sort()
5        l, r = 0,len(people)-1
6
7        while l <=r:
8            if people[l] + people[r] <= limit:
9                l+=1
10                r-=1
11                res +=1
12            else:
13                r-=1
14                res +=1
15        return res
16