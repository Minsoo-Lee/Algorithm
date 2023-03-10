# node 클래스 :
# int data, Node left, Node right

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# BST 탐색
def getNodeOrNull(node, data):
        if node == None:
            return None
        if node.data == data:
            return node
        if data < node.data:
            return getNodeOrNull(node.left, data)
        return getNodeOrNull(node.right, data)
    
# 중위 순회
def traverse_in_order(node):
    if node == None:
        return 
        
    traverse_in_order(node.left)
    print(node.data)
    traverse_in_order(node.right)