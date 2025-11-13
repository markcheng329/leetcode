# Last updated: 11/13/2025, 6:54:03 AM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def backtracking(left,right):
            if len(subset) == 2 * n:
                res.append("".join(subset))
                return 
            
            if left < n:
                subset.append("(")
                backtracking(left+1,right)
                subset.pop()
            
            if right < left:
                subset.append(")")
                backtracking(left,right+1)
                subset.pop()
        
        backtracking(0,0)
        return res