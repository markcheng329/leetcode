# Last updated: 1/2/2026, 5:40:13 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        
9        dummy = ListNode()
10        tail = dummy
11
12        while list1 and list2:
13            if list1.val > list2.val:
14                tail.next = list2
15                list2 = list2.next
16            else:
17                tail.next = list1
18                list1 = list1.next
19            tail = tail.next
20
21        tail.next = list1 or list2
22        return dummy.next