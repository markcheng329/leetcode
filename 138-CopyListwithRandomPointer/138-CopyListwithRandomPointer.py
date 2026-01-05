# Last updated: 1/5/2026, 1:18:48 AM
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
15        #A-A'-B-B'-C-C'
16        
17        l1 = head
18        while l1:
19            l2 = Node(l1.val)
20            l2.next = l1.next
21            l1.next = l2
22            l1 = l2.next
23        
24        newhead = head.next
25
26        l1 = head
27        while l1:
28            if l1.random:
29                l1.next.random = l1.random.next
30            l1= l1.next.next
31        
32        newhead = head.next
33        
34        l1 = head
35        while l1:
36            l2 = l1.next
37            l1.next = l2.next
38            if l2.next:
39                l2.next = l2.next.next
40            l1 = l1.next
41        
42        return newhead