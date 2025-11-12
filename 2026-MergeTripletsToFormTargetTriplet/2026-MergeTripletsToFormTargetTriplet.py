# Last updated: 11/12/2025, 4:56:56 AM
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        answer = set()


        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            if t[0] == target[0]:
                answer.add(0)
            if t[1] == target [1]:
                answer.add(1)
            if t[2] == target[2]:
                answer.add(2)
        return True if len(answer) == 3 else False