# Last updated: 12/2/2025, 2:27:12 AM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        count = {}
4        maxf = 0
5        l = 0
6        res = 0
7
8        for i in range(len(s)):
9            count[s[i]] = count.get(s[i],0) +1
10            maxf = max(maxf,count[s[i]])
11
12            if (i - l + 1) - maxf > k:
13                count[s[l]] -=1
14                l +=1
15            
16            res = max(res,i-l+1)
17        return res