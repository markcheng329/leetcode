# Last updated: 1/28/2026, 11:38:31 AM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        words = set(wordDict)
4        lens = set(len(w) for w in words)
5        q = deque([0])
6        visit =set()
7        n = len(s)
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
20                    q.append(end)
21        return False