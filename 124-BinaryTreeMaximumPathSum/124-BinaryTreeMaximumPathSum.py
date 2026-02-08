# Last updated: 2/7/2026, 9:51:42 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        best = float("-inf")
10
11        def dfs(node):
12            nonlocal best
13            if not node:
14                return 0
15            
16            left = max(0,dfs(node.left))
17            right = max(0,dfs(node.right))
18
19            best = max(best,node.val+left+right)
20            return node.val + max(left,right)
21        dfs(root)
22        return best
23