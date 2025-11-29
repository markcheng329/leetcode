# Last updated: 11/29/2025, 1:23:08 AM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        i , j = 0,0
4        res = []
5
6        while i < len(word1) or i < len(word2):
7            if i < len(word1):
8                res.append(word1[i])
9            if j < len(word2):
10                res.append(word2[j])
11            
12            i +=1
13            j +=1
14        return "".join(res)
15
16
17