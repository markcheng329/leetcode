# Last updated: 2/7/2026, 9:54:47 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9
10    def serialize(self, root):
11        """Encodes a tree to a single string.
12        
13        :type root: TreeNode
14        :rtype: str
15        """
16        if not root:
17            return ""
18        q = deque([root])
19        out = []
20        while q:
21            node = q.popleft()
22            if node:
23                out.append(str(node.val))
24                q.append(node.left)
25                q.append(node.right)
26            else:
27                out.append("#")
28        return ",".join(out)
29        
30
31    def deserialize(self, data):
32        """Decodes your encoded data to tree.
33        
34        :type data: str
35        :rtype: TreeNode
36        """
37        if not data:
38            return None
39        vals = data.split(",")
40        root = TreeNode(int(vals[0]))
41        q = deque([root])
42        i = 1
43        while q:
44            node = q.popleft()
45
46            # left
47            if vals[i] != "#":
48                node.left = TreeNode(int(vals[i]))
49                q.append(node.left)
50            i += 1
51
52            # right
53            if vals[i] != "#":
54                node.right = TreeNode(int(vals[i]))
55                q.append(node.right)
56            i += 1
57
58        return root
59        
60
61# Your Codec object will be instantiated and called as such:
62# ser = Codec()
63# deser = Codec()
64# ans = deser.deserialize(ser.serialize(root))