# Last updated: 1/27/2026, 4:37:34 AM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        words = set(wordDict)
4        n = len(s)
5
6        q = deque([0])      # 队列里存：当前能到达的下标
7        visited = set()    # 记录已经处理过的起点
8
9        while q:
10            start = q.popleft()
11            if start in visited:
12                continue
13            visited.add(start)
14
15            for end in range(start + 1, n + 1):
16                if s[start:end] in words:
17                    if end == n:
18                        return True
19                    q.append(end)
20
21        return False