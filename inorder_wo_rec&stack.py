class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def morris_tree_traversal(root):
    cur = root
    while cur is not None:
        if cur.left is None:
            print(cur.data)
            cur = cur.right
        else:
            pre = cur.left
            while pre.right is not None and pre.right != cur:
                pre = pre.right
            if pre.right is None:
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                print(cur.data)
                cur = cur.right


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(2)
    root.right = Node(10)
    root.right.left = Node(9)
    root.right.right = Node(20)

    morris_tree_traversal(root)