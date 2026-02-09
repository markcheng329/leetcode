# Last updated: 2/8/2026, 7:20:43 PM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        freq = Counter(tasks)
4        maxFreq = max(freq.values())
5        maxCount = sum(1 for v in freq.values() if v == maxFreq)
6
7        # Frame length based on the most frequent tasks
8        frame = (maxFreq - 1) * (n + 1) + maxCount
9
10        # Can't be shorter than total tasks (when fillers remove idles)
11        return max(len(tasks), frame)