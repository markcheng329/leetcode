# Last updated: 12/10/2025, 9:00:56 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(t) != len(s) :
4            return False
5        
6        count = {}
7
8        for i in range(len(t)):
9            count[t[i]] = count.get(t[i],0) + 1
10
11        for i in range(len(s)):
12            if s[i] not in count:
13                return False
14            count[s[i]] -=1
15            if count[s[i]] < 0:
16                return False
17        return True
18            