# Last updated: 11/12/2025, 4:57:34 AM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        have = [0] * 26
        need = [0] * 26

        for i in s1:
            need[ord(i)- ord("a")] +=1
        
        for i in range(len(s1)):
            have[ord(s2[i])-ord("a")] +=1
        
        if need == have:
            return True
        
        for i in range(len(s1),len(s2)):
            have[ord(s2[i])-ord("a")] +=1
            have[ord(s2[i-len(s1)])-ord("a")] -=1

            if have == need:
                return True
        return False
