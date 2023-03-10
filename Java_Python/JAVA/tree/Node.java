package JAVA.tree;

public class Node {
    public int data;
    public Node left;
    public Node right;

    // BST 탐색
    public static Node getNodeOrNull(Node node, int data) {
        if (node == null)
            return null;
        if (node.data == data)
            return node;
        if (data < node.data)
            return getNodeOrNull(node.left, data);
        return getNodeOrNull(node.right, data);
    }

    // 트리 순회 - 중위 순회
    public static void traverse_in_order(Node node) {
        if (node == null)
            return ;
        
        traverse_in_order(node.left);
        System.out.println(node.data);
        traverse_in_order(node.right);
    }
}

// BST 탐색 코드