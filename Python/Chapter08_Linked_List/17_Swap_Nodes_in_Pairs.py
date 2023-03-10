# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tmp = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            prev.next = head.next
            head.next = prev.next.next
            prev.next.next = head
            
            head = head.next
            prev = prev.next.next
            
        return (tmp.next)
        
        