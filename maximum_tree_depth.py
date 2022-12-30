class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def tree_depth(root):
    if root == None:
        return
    left_depth = tree_depth(root.left)
    right_depth = tree_depth(root.right)
    if left_depth > right_depth:
        return left_depth+1
    else:
        return right_depth+1
    #return 1+max(left_depth, right_depth)


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(2)
    root.left.right.left = Node(6)
    root.right = Node(10)
    root.right.left = Node(9)
    root.right.right = Node(20)
    print(tree_depth(root))