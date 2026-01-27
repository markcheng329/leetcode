# Last updated: 1/27/2026, 4:49:33 AM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        words = set(wordDict)
4        n = len(s)
5        lens = set(len(w) for w in words)
6        q = deque([0])
7        visit = set()
8
9        while q:
10            start = q.popleft()
11            if start in visit:
12                continue
13            visit.add(start)
14
15            for l in lens:
16                end = start + l
17                if end <= n and s[start:end] in words:
18                    if end == n:
19                        return True
20                    
21                    q.append(end)
22        return False