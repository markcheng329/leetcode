# Last updated: 11/13/2025, 4:46:19 AM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_l,best_len = 0,0
        
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > best_len:
                    best_len = r-l+1
                    best_l = l

                l -=1
                r+=1

        for i in range(len(s)):
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > best_len:
                    best_len = r-l+1
                    best_l = l              
                l -=1
                r+=1

        return s[best_l:best_l + best_len]