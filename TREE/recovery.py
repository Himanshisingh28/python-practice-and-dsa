
class Solution(object):
    def __init__(self):
        self.prev = None
        self.first = None
        self.second = None
        self.count = 0

    def inOrder(self, root):
        if root is None:
            return

        self.inOrder(root.left)

        if self.prev is None:
            self.prev = root
        else:
            if root.val < self.prev.val:
                if self.count == 0:
                    self.first = self.prev
                    self.second = root
                else:
                    self.second = root
                self.count += 1

            self.prev = root

        self.inOrder(root.right)

    def recoverTree(self, root):
        self.inOrder(root)

        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
        
