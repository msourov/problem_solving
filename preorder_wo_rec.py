class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def preorder(root):
    if root is None:
        return
    s = []
    s.append(root)
    temp = root
    while s:
        if temp:
            print(temp.data, end=' ')
            if temp.right:
                s.append(temp.right)
            temp = temp.left
        else:
            temp = s.pop()


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(2)
    root.right = Node(10)
    root.right.left = Node(9)
    root.right.right = Node(20)

    preorder(root)