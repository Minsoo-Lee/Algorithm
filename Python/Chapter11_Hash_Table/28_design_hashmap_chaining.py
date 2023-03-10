import collections
from LinkedList import ListNode

class my_hashmap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        # collections.defaultdict: 존재하지 않는 키 조회시 자동으로 디폴트 생성
    def put(self, key:int, value:int):
        index = key % self.size
        # 인덱스에 노드가 없으면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return 
        # 인덱스에 노드가 존재하는 경우 연결리스트로 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key:int):
        index = key % self.size
        if self.table[index].value is None:
            return -1
        #노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key:int):
        index = key % self.size
        if self.table[index].value is None:
            return
        #인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
