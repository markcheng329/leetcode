# Last updated: 1/6/2026, 12:54:37 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        slow,fast = head,head
12        while fast and fast.next:
13            slow = slow.next
14            fast = fast.next.next
15        
16        prev,cur = None,slow.next
17        slow.next = None
18        while cur:
19            temp = cur.next
20            cur.next = prev
21            prev = cur
22            cur = temp
23        
24        first,second = head,prev
25        while second:
26            temp1 = first.next
27            temp2 = second.next
28            first.next = second
29            second.next = temp1
30            first = temp1
31            second = temp2