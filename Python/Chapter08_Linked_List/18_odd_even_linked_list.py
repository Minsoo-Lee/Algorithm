# 328. Odd Even Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        even = ListNode(None)
        even_tmp = even
        odd = ListNode(None)
        odd_tmp = odd
        count = 1
        while head:
            if count % 2 == 0:
                odd_tmp.next = ListNode(head.val)
                odd_tmp = odd_tmp.next
            else:
                even_tmp.next = ListNode(head.val)
                even_tmp = even_tmp.next
            head = head.next
            count += 1
            
        result = ListNode(None)
        result_tmp = result
        while even.next:
            result_tmp.next = ListNode(even.next.val)
            result_tmp = result_tmp.next
            even = even.next
        while odd.next:
            result_tmp.next = ListNode(odd.next.val)
            result_tmp = result_tmp.next
            odd = odd.next
        return result.next
        