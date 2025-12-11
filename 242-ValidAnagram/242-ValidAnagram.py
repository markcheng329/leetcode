# Last updated: 12/10/2025, 8:52:02 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        count1 = Counter(t)
4
5        count2 = Counter(s)
6
7        if count1 != count2 :
8            return False
9        else:
10            return True