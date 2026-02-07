# Last updated: 2/7/2026, 4:19:29 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11
12        res = []
13        q = deque([root])
14
15        while q:
16            level_size = len(q)
17
18            for i in range(level_size):
19                node = q.popleft()
20
21                if node.left:
22                    q.append(node.left)
23                if node.right:
24                    q.append(node.right)
25
26                # 这一层最后一个节点
27                if i == level_size - 1:
28                    res.append(node.val)
29
30        return res