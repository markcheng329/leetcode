# Last updated: 1/27/2026, 5:06:14 AM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        words = set(wordDict)
4        lens = set(len(w) for w in words)
5        q = deque([0])
6        visit = set()
7        n = len(s)
8        
9
10        while q:
11            start = q.popleft()
12            if start in visit:
13                continue
14            visit.add(start)
15
16            for l in lens:
17                end = start+l
18                if end <= n and s[start:end] in words:
19                    if end == n:
20                        return True
21                    
22                    q.append(end)
23        return False
24