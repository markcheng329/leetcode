# Last updated: 11/24/2025, 10:32:46 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        count = Counter(s)

        for i in range(len(t)):
            if t[i] in count and count[t[i]] > 0:
                count[t[i]] -=1
            else:
                return False
        return True