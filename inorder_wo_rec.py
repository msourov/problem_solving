class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def InOrder(root):
    s = []
    s.append(root)
    while s is not None:
        if root.left:
            s.append(root.left)
            root = root.left
        elif s:
            root = s.pop()
            print(root.data)
            if root.right:
                s.append(root.right)
                root = root.right
        else:
            break


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.left.right = Node(2)
    root.left.left = Node(4)
    root.right = Node(10)
    root.right.left = Node(9)
    root.right.right = Node(20)

    InOrder(root)