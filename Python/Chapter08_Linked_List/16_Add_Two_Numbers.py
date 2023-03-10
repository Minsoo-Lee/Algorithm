# 2. Add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        tmp = result
        ten = 0
        while l1 and l2:
            value = l1.val + l2.val
            one = (value + ten) % 10
            tmp.next = ListNode(one)
            ten = (value + ten) // 10
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                print("HOW")
                value = l1.val
                one = (value + ten) % 10
                tmp.next = ListNode(one)
                ten = (value + ten) // 10
                l1 = l1.next
                tmp = tmp.next
        if l2:
            while l2:
                value = l2.val
                one = (value + ten) % 10
                tmp.next = ListNode(one)
                ten = (value + ten) // 10
                l2 = l2.next
                tmp = tmp.next
        if ten == 1:
            tmp.next = ListNode(1)
        return result.next
            
            