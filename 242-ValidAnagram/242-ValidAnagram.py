# Last updated: 12/6/2025, 10:24:00 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3
4        if len(s) != len(t):
5            return False
6
7        count = {}
8
9        for i in range(len(t)):
10            count[t[i]] = count.get(t[i],0) +1
11        
12        for i in range(len(s)):
13            if s[i] not in count:
14                return False
15            count[s[i]] -=1
16            if count[s[i]] < 0:
17                return False
18        return True