# Last updated: 11/14/2025, 8:52:28 PM
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for i in range(len(tasks)):
            count[ord(tasks[i])-ord("A")] +=1
        
        maxf = max(count)
        maxc = 0
        for i in count:
            maxc +=1 if i == maxf else 0
        
        res = (maxf-1)*(n+1) + maxc
        return max(len(tasks),res)
        


