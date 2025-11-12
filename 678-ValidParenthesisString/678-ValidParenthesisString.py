# Last updated: 11/12/2025, 4:57:29 AM
class Solution:
    def checkValidString(self, s: str) -> bool:
        lmin,lmax = 0,0

        for i in range(len(s)):
            c = s[i]

            if c == "(":
                lmin +=1
                lmax +=1
            elif c == ")":
                lmin -=1
                lmax -=1
            else:
                lmin -=1
                lmax +=1
            
            if lmax < 0:
                return False
            
            if lmin < 0:
                lmin = 0
        return True if lmin == 0 else False