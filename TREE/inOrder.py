
class Solution(object):
    def __init__(self):
        self.ans=[]
    
    def inOrder(self,root):
        if root is None:
            return
        self.inOrder(root.left)
        self.ans.append(root.val)
        self.inOrder(root.right)

    def inorderTraversal(self, root):
        self.inOrder(root)
        return self.ans