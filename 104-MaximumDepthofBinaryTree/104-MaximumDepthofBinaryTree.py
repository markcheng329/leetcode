# Last updated: 2/7/2026, 3:15:36 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        
12        q = deque([root])
13        depth = 0
14
15        while q:
16            depth +=1
17            for i in range(len(q)):
18                node = q.popleft()
19                
20                if node.left:
21                    q.append(node.left)
22                if node.right:
23                    q.append(node.right)
24        return depth
25
26            
27