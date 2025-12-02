# Last updated: 12/1/2025, 11:27:24 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        i, j = 0,0
4        res = []
5
6        while i < len(word1) or j < len(word2):
7            if i < len(word1):
8                res.append(word1[i])
9                i +=1
10            
11            if j < len(word2):
12                res.append(word2[j])
13                j+=1
14        return "".join(res)
15
16            