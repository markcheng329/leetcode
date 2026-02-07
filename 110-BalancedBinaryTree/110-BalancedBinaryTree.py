# Last updated: 2/7/2026, 3:30:58 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def dfs(node: Optional[TreeNode]) -> int:
10            if not node:
11                return 0  # 空树高度为 0
12
13            lh = dfs(node.left)
14            if lh == -1:
15                return -1  # 左子树已不平衡，直接剪枝
16
17            rh = dfs(node.right)
18            if rh == -1:
19                return -1  # 右子树已不平衡，直接剪枝
20
21            if abs(lh - rh) > 1:
22                return -1  # 当前节点不平衡
23
24            return 1 + max(lh, rh)  # 返回当前高度
25
26        return dfs(root) != -1