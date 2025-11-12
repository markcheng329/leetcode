# Last updated: 11/12/2025, 4:57:15 AM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l,r=0,len(people)-1

        while l <= r:
            remain = limit - people[r]
            r -=1
            res +=1
            if l <= r and remain >= people[l]:
                l +=1
        return res