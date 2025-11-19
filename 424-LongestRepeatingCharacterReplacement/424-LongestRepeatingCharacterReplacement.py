# Last updated: 11/19/2025, 1:41:42 AM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = {}
        maxf = 0


        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1
            maxf = max(maxf,count[s[i]])

            while (i-l+1) -maxf > k:
                count[s[l]] -=1
                l +=1
            res = max(res,i-l+1)
        return res