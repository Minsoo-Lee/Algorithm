from LinkedList import *

class MyCircularDeque:
    def __init__(self, k):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
  
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new
    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insert_front(self, value: int):
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
    def insert_last(self, value: int):
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def delete_front(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True
    def delete_last(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
    
    def get_front(self):
        return self.head.right.val if self.len else -1
    def get_rear(self):
        return self.tail.left.val if self.len else -1
    def is_empty(self):
        return self.len == 0
    def is_full(self):
        return self.len == self.k