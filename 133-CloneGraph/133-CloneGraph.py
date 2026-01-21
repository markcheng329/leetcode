# Last updated: 1/21/2026, 1:28:20 AM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        if not node:
13            return None
14        
15        oldtonew = {}
16
17        def dfs(node):
18            if node in oldtonew:
19                return oldtonew[node]
20            
21            copy = Node(node.val)
22            oldtonew[node] = copy
23
24            for nei in node.neighbors:
25                copy.neighbors.append(dfs(nei))
26            return copy
27        return dfs(node)
28            