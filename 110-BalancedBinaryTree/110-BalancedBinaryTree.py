# Last updated: 2/7/2026, 3:36:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def dfs(node):
10            if not node:
11                return 0
12            
13            lh = dfs(node.left)
14            if lh == -1:
15                return -1
16            
17            rh = dfs(node.right)
18            if rh == -1:
19                return -1
20            
21            if abs(rh-lh) > 1:
22                return -1
23            
24            return 1+max(rh,lh)
25        return dfs(root) != -1
26            
27