# Last updated: 1/6/2026, 1:39:35 AM
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
15            val = v1+v2+carry
16
17            carry = val // 10
18            val = val % 10
19
20            tail.next = ListNode(val)
21            tail = tail.next
22
23            l1 = l1.next if l1 else None
24            l2 = l2.next if l2 else None
25        return dummy.next