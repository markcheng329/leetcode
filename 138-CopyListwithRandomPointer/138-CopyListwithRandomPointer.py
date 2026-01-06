# Last updated: 1/6/2026, 1:33:29 AM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        if not head:
13            return None
14        
15        l1 = head
16        while l1:
17            l2 = Node(l1.val)
18            l2.next = l1.next
19            l1.next = l2
20            l1 = l2.next
21        
22        l1 = head
23        while l1:
24            if l1.random:
25                l1.next.random = l1.random.next
26            l1 = l1.next.next
27        
28        newhead = head.next
29
30        l1 = head
31        while l1:
32            l2 = l1.next
33            l1.next = l2.next
34            if l2.next:
35                l2.next = l2.next.next
36            l1 = l1.next
37        
38        return newhead
39