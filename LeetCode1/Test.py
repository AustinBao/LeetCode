# Prints the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Preorder traversal (Root -> Left ->Right)
    def PreorderTraversal(self, root):
        storage = []
        if root:
            storage.append(root.data)
            storage = storage + self.PreorderTraversal(root.left)
            storage = storage + self.PreorderTraversal(root.right)
        return storage
