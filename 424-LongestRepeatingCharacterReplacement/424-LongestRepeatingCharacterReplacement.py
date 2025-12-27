# Last updated: 12/27/2025, 2:03:56 AM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        res = 0
4        count = {}
5        maxf = 0
6        l = 0
7
8        for i in range(len(s)):
9            count[s[i]] = count.get(s[i],0) +1
10            maxf = max(maxf,count[s[i]])
11            
12            while (i-l + 1) - maxf > k:
13                count[s[l]] -=1
14                l +=1
15            res = max(res,i-l+1)
16        return res
17            
18
19            