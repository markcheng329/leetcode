# Last updated: 1/13/2026, 1:19:57 AM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        res = []
4        subset = []
5
6        phone = {
7            "2": "abc",
8            "3": "def",
9            "4": "ghi",
10            "5": "jkl",
11            "6": "mno",
12            "7": "pqrs",
13            "8": "tuv",
14            "9": "wxyz",
15        }
16        
17        def dfs(i):
18            if i == len(digits):
19                res.append("".join(subset))
20                return
21            
22            for ch in phone[digits[i]]:
23                subset.append(ch)
24                dfs(i+1)
25                subset.pop()
26        
27        dfs(0)
28        return res
29