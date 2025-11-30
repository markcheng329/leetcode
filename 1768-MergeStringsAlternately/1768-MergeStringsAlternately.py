# Last updated: 11/30/2025, 1:56:43 AM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        res = []
4
5        i, j = 0,0
6
7        while i < len(word1) and j < len(word2):
8            res.append(word1[i])
9            res.append(word2[j])
10            i +=1
11            j+=1
12        
13        res.append(word1[i:]) or res.append(word2[j:])
14        
15
16        return "".join(res)