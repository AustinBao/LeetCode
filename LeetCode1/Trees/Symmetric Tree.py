class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def isSymmetric(self, root):
      if root is None:
        return True
      else:
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
      if left is None and right is None:
        return True
      if left is None or right is None:
        return False

      if left.data == right.data:
        outPair = self.isMirror(left.left, right.right)
        inPiar = self.isMirror(left.right, right.left)

        return outPair and inPiar
      else:
        return False


root = Node(1)
root.right = Node(2)
root.left = Node(2)
root.left.left = Node(3)
# root.left.right = Node(4)
# root.right.left = Node(4)
root.right.right = Node(3)
print(root.isSymmetric(root))



