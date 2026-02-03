# Last updated: 2/2/2026, 7:16:43 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        i,j =0,0
4        res = []
5
6        while i < len(word1) and j < len(word2):
7            if i <= j :
8                res.append(word1[i])
9                i +=1
10            else:
11                res.append(word2[j])
12                j +=1
13        
14        while i < len(word1):
15            res.append(word1[i])
16            i +=1
17        
18        while j < len(word2):
19            res.append(word2[j])
20            j+=1
21        
22        return "".join(res)
23