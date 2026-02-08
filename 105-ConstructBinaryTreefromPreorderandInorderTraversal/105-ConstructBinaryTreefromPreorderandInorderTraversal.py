# Last updated: 2/7/2026, 10:03:12 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        if not preorder:
10            return None
11
12        root = TreeNode(preorder[0])
13        stack = [root]
14        in_i = 0
15
16        pre_i = 1
17        n = len(preorder)
18
19        while pre_i < n:
20            node = TreeNode(preorder[pre_i])
21            pre_i += 1
22
23            top = stack[-1]
24            if top.val != inorder[in_i]:
25                # 还在构建左链：直接挂到左边
26                top.left = node
27                stack.append(node)
28            else:
29                # 左边结束：不断弹栈，找到该挂右孩子的父节点
30                while stack and stack[-1].val == inorder[in_i]:
31                    top = stack.pop()
32                    in_i += 1
33                top.right = node
34                stack.append(node)
35
36        return root