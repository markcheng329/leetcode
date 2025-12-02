# Last updated: 12/2/2025, 2:34:05 AM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3
4        if len(s1) > len(s2):
5            return False
6        
7        have = [0] * 26
8        need = [0] * 26
9
10        for i in range(len(s1)):
11            need[ord(s1[i])-ord("a")] +=1
12        
13        for i in range(len(s1)):
14            have[ord(s2[i]) - ord ("a")] +=1
15
16        if need == have:
17            return True
18        
19        for i in range(len(s1),len(s2)):
20            have[ord(s2[i]) - ord ("a")] +=1
21            have[ord(s2[i-len(s1)]) - ord ("a")] -=1
22
23            if have == need:
24                return True
25        return False