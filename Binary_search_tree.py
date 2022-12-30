class Node:
    def __init__(self, value = None):
        self.value = value
        self.l = None
        self.r = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur):
        if value < cur.value:
            if cur.l is None:
                cur.l = Node(value)
                cur.l.parent = cur  #set parent
            else:
                self._insert(value, cur.l)
        elif value > cur.value:
            if cur.r is None:
                cur.r = Node(value)
                cur.r.parent = cur #set parent
            else:
                self._insert(value, cur.r)
        else:
            print('Value already in tree')

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur):
        if value == cur.value:
            return cur
        elif value < cur.value and cur.l is not None:
            return self._find(value, cur.l)
        elif value > cur.value and cur.r is not None:
            return self._find(value, cur.r)

    def find_minimum(self, n):
        cur = n
        while cur.l is not None:
            cur = cur.l
        return cur

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        if node is None or self.find(node.value) is None:
            print('Node to be deleted is not found in the tree!')
            return None

        def num_children(n):
            num_children = 0
            if n.l is not None: num_children += 1
            if n.r is not None: num_children += 1
            return num_children
        node_parent = node.parent
        node_children = num_children(node)
        if node_children == 0:
            node_parent.l = None
        else:
            node_parent.r = None
        if node_children == 1:
            if Node.l is not None:
                child = node.l
            else:
                child = node.r
            if node_parent.l == Node:
                node_parent.l = child
            else:
                node_parent.r = child
            child.parent = node_parent

        if node_children == 2:
            successor = self.find_minimum(Node.r)
            Node.value = successor.value
            self.delete_node(successor)

    def search(self, value):
        if self.root is not None:
            ans = self._search(value, self.root)
            if ans:
                print('Found')
            else:
                print('Not Found')
        else:
            return False

    def _search(self, value, cur):
        if value == cur.value:
            return True
        elif value < cur.value and cur.l is not None:
            return self._search(value, cur.l)
        elif value > cur.value and cur.r is not None:
            return self._search(value, cur.r)
        return False

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.l)
            print(root.value,end=' ')
            self.inorder_traversal(root.r)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur):
        if cur is not None:
            self._print_tree(cur.l)
            print(str(cur.value))
            self._print_tree(cur.r)

    def inOrderSuccessor(self, root, n):

        # Step 1 of the above algorithm
        if n.r is not None:
            return self.find_minimum(n.r)

            # Step 2 of the above algorithm
        p = n.parent
        while p is not None:
            if n != p.r:
                break
            n = p
            p = p.parent
        return p

tree = BST()
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(10)
tree.insert(9)
tree.insert(11)
tree.delete_value(4)
tree.print_tree()
tree.inorder_traversal(tree.root)
print(f'\nMinimum value of tree is: {tree.find_minimum(tree.root).value}\n')
print(tree.inOrderSuccessor(tree.root, 10))