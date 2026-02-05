# Last updated: 2/5/2026, 8:51:36 AM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        cnt = Counter(tasks)
4        maxFreq = max(cnt.values())
5        maxCount = sum(1 for v in cnt.values() if v == maxFreq)
6
7        # 骨架长度 vs 任务总数，取更大者
8        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)