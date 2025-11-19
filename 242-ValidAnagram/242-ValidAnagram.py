# Last updated: 11/18/2025, 8:47:15 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s) :
            return False
        
        count = Counter(s)

        for i in t:
            count[i] -=1
            if count[i] < 0:
                return False
        return True