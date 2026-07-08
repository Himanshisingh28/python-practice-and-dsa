class Solution(object):
    def __init__(self):
        self.ans=[]

    def postOrder(self, root):
        if root is None:
            return 
        self.postOrder(root.left)
        self.postOrder(root.right)
        self.ans.append(root.val)

    def postorderTraversal(self, root):
        self.postOrder(root)
        return self.ans