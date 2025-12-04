# Last updated: 12/3/2025, 9:06:37 PM
1class Solution:
2    def checkInclusion(self, s1: str, s2: str) -> bool:
3        if len(s1) > len(s2):
4            return False
5        
6        have = [0] * 26
7        need = [0] * 26
8
9        for i in range(len(s1)):
10            need[ord(s1[i])-ord("a")] +=1
11        
12        for i in range(len(s1)):
13            have[ord(s2[i])-ord("a")] +=1
14        
15        if need == have:
16            return True
17        
18        for i in range(len(s1),len(s2)):
19            have[ord(s2[i])-ord("a")] +=1
20            have[ord(s2[i-len(s1)])-ord("a")] -=1
21
22            if have == need:
23                return True
24        return False
25