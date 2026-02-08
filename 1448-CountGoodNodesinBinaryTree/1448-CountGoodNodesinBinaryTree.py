# Last updated: 2/7/2026, 8:57:26 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        def dfs(node,maxval):
10            if not node:
11                return 0
12            
13            good = 1 if node.val >= maxval else 0
14
15            maxval = max(node.val,maxval)
16
17            return good + dfs(node.left,maxval) + dfs(node.right,maxval)
18        
19        return dfs(root,root.val)