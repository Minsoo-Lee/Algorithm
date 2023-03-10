import heapq
from LinkedList import *

def merge_k_lists(self, lists):
    root = result = ListNode(None)
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (list[i].val, i, lists[i]))
    while heap:
        node = heapq.heapppop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heapush(heap, (result.next.val, idx, result.next))

    return root.next
            

