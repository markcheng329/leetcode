# Last updated: 11/12/2025, 4:57:02 AM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxn = curn = 0
        vowel = "aeiou"

        for i in range(len(s)):
            if s[i] in vowel:
                curn +=1
            
            if i < k-1:
                continue
            
            maxn = max(maxn,curn)

            if s[i-k+1] in vowel:
                curn -=1
        
        return maxn
            