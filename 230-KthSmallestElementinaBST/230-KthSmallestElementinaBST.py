# Last updated: 2/7/2026, 9:36:16 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        stack = []
10        cur = root
11
12        while stack or cur:
13            while cur:
14                stack.append(cur)
15                cur = cur.left
16
17            cur = stack.pop()
18            k -=1
19            if k == 0:
20                return cur.val
21            
22            cur = cur.right