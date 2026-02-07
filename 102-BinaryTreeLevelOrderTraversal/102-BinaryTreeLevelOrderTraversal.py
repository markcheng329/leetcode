# Last updated: 2/7/2026, 4:16:48 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return []
11        q = deque([root])
12        res = []
13        while q:
14            level = []
15            for i in range(len(q)):
16                node = q.popleft()
17                level.append(node.val)
18                if node.left:
19                    q.append(node.left)
20                if node.right:
21                    q.append(node.right)
22            res.append(level)
23        return res
24
25        
26