# Last updated: 11/12/2025, 4:57:21 AM
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {}
        for i in range(len(s)):
            c = s[i]
            lastindex[c] = i
        
        res = []
        end = 0
        size = 0

        for i in range(len(s)):
            c = s[i]
            size +=1
            end = max(end,lastindex[c])

            if i == end:
                res.append(size)
                size = 0
        return res
