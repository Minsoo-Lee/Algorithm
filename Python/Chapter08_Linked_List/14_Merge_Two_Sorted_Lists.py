# 21. Merge Two Sorted Lists

#Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        new_node = ListNode(0)
        tmp = new_node
        while list1 and list2:
            if list1.val >= list2.val:
                value = list2.val
                list2 = list2.next
            else:
                value = list1.val
                list1 = list1.next
            tmp.next = ListNode(value)
            tmp = tmp.next
        if list1:
            while list1:
                tmp.next = ListNode(list1.val)
                tmp, list1 = tmp.next, list1.next
        if list2:
            while list2:
                tmp.next = ListNode(list2.val)
                tmp, list2 = tmp.next, list2.next
        return new_node.next