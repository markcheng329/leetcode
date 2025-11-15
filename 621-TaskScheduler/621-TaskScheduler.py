# Last updated: 11/14/2025, 8:45:29 PM
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        maxf = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxf else 0

        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)