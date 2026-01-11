# Last updated: 1/11/2026, 8:10:07 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9        if not subRoot:
10            return True
11        if not root:
12            return False
13        
14        if self.isSameTree(root,subRoot):
15            return True
16
17        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
18
19
20
21    def isSameTree(self,root,subRoot):
22        if not root and not subRoot:
23            return True
24        if not root or not subRoot:
25            return False
26        
27        if root.val != subRoot.val:
28            return False
29        
30        return self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right)
31