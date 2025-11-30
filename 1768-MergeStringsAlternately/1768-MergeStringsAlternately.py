# Last updated: 11/30/2025, 1:58:28 AM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        res = []
4
5        i, j = 0,0
6
7        while i < len(word1) or j < len(word2):
8            if i < len(word1):
9                res.append(word1[i])
10            if j < len(word2):
11                res.append(word2[j])
12
13            i +=1
14            j +=1
15
16        return "".join(res)