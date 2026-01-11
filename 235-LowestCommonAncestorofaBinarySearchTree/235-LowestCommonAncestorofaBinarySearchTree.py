# Last updated: 1/11/2026, 8:15:24 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        cur = root
11
12        while cur:
13            if p.val > cur.val and q.val > cur.val:
14                cur = cur.right
15            elif p.val < cur.val and q.val < cur.val:
16                cur = cur.left
17            else:
18                return cur