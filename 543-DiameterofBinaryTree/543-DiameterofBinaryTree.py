# Last updated: 2/7/2026, 3:26:42 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        res = 0
10
11        def height(node):
12            nonlocal res
13
14            if not node:
15                return 0
16            
17            lh = height(node.left)
18            rh = height(node.right)
19
20            res = max(res,lh+rh)
21            return 1 + max(lh,rh)
22        
23        height(root)
24        return res