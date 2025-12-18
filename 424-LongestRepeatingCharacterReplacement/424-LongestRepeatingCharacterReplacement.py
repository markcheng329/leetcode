# Last updated: 12/18/2025, 12:37:38 AM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        l = 0
4        res = 0
5        maxf = 0
6        count = {}
7
8        for i in range(len(s)):
9            count[s[i]] = count.get(s[i],0) + 1
10            maxf = max(maxf,count[s[i]])
11
12            while (i-l+1)-maxf > k:
13                count[s[l]] -=1
14                l +=1
15                
16            res = max(res,i-l+1)
17        return res
18
19