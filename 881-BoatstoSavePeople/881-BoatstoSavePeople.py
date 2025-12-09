# Last updated: 12/9/2025, 6:14:20 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        res = 0
5
6        l, r = 0,len(people)-1
7
8        while l <= r:
9            if people[l] + people[r] <= limit:
10                l +=1
11                r-=1
12            else:
13                r-=1
14            res +=1
15        return res