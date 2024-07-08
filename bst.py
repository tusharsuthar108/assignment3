class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def print(self):
        self.print_leaf_nodes1(self.root)

    def print_leaf_nodes1(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.key, end=" ")
        self.print_leaf_nodes1(node.left)
        self.print_leaf_nodes1(node.right)

bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(6)
bst.insert(8)
bst.print()
