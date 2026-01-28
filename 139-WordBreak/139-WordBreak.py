# Last updated: 1/28/2026, 11:19:06 AM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        words = set(wordDict)
4        n = len(s)
5        lens = set(len(w) for w in words)
6        q = deque([0])
7        visit = set()
8
9
10        while q:
11            start = q.popleft()
12            if start in visit:
13                continue
14            visit.add(start)
15
16            for l in lens:
17                end = start + l
18                if end <= n and s[start:end] in words:
19                    if end == n:
20                        return True
21                    q.append(end)
22        return False
23
24
25
26