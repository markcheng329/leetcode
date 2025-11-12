# Last updated: 11/12/2025, 4:57:23 AM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            
            else:
                stack.append(i)
        return res


            