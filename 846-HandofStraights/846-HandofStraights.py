# Last updated: 1/9/2026, 10:15:59 PM
1class Solution:
2    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
3        if len(hand) % groupSize != 0:
4            return False
5
6        count = Counter(hand)
7
8        for num in sorted(hand):
9            if count[num]:
10                for i in range(num, num + groupSize):
11                    if not count[i]:
12                        return False
13                    else:
14                        count[i] -=1
15        return True