# Last updated: 1/5/2026, 2:06:51 AM
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
15        #a-a'-b-b'-c-c'
16        
17        l1 = head
18        while l1:
19            l2 = Node(l1.val)
20            l2.next = l1.next
21            l1.next = l2
22            l1 = l2.next
23        
24        l1 = head
25        while l1:
26            if l1.random:
27                l1.next.random = l1.random.next
28            l1 = l1.next.next
29        
30        newhead = head.next
31
32        l1= head
33        while l1:
34            l2 = l1.next
35            l1.next = l2.next
36            if l2.next:
37                l2.next = l2.next.next
38            l1 = l1.next
39        
40        return newhead
41
42