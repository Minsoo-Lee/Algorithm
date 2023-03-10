# 92. Reverse Linked List II

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        tmp = head
        count = 1
        result = ListNode(None)
        result_tmp = result
        while tmp and count < left:
            result_tmp.next = ListNode(tmp.val)
            result_tmp = result_tmp.next
            tmp = tmp.next
            count += 1

        rev = None
        while tmp and count < right + 1:
            rev, rev.next, tmp = tmp, rev, tmp.next
            count += 1
            
        while rev:
            result_tmp.next = ListNode(rev.val)
            rev = rev.next
            result_tmp = result_tmp.next
        while tmp:
            result_tmp.next = ListNode(tmp.val)
            tmp = tmp.next
            result_tmp = result_tmp.next
        return result.next
        
        
        