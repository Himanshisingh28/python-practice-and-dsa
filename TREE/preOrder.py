
class Solution(object):
    def __init__(self):
        self.ans=[]

    def preOrder(self,root):
        if root is None:
            return 
        self.ans.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def preorderTraversal(self, root):
        self.preOrder(root)
        return self.ans
        