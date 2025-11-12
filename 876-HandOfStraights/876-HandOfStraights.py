# Last updated: 11/12/2025, 4:57:17 AM
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for num in sorted(hand):
            if count[num]:
                for i in range(num,num+groupSize):
                    if not count[i]:
                        return False
                    else:
                        count[i] -=1
        return True