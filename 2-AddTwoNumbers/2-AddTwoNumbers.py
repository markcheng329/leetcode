# Last updated: 1/5/2026, 2:23:10 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode()
9        tail = dummy
10        carry = 0
11
12        while l1 or l2 or carry:
13            v1 = l1.val if l1 else 0
14            v2 = l2.val if l2 else 0
15
16            val = v1+v2+carry
17            
18            carry = val // 10
19            val = val % 10
20
21            tail.next = ListNode(val)
22            tail = tail.next
23
24            l1 = l1.next if l1 else None
25            l2 = l2.next if l2 else None
26        return dummy.next
27            
28
29