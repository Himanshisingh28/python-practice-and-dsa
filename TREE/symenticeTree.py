class Solution(object):
    def solve(self, root1, root2):
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        if root1.val!=root2.val:
            return False
        r1=self.solve(root1.left, root2.right)
        r2=self.solve(root1.right, root2.left)

        if r1==True and r2==True:
            return True
        else:
            return False
    def isSymmetric(self, root):
        return self.solve(root.left, root.right)