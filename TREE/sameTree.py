
class Solution(object):
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.val!=q.val:
            return False
        r1=self.isSameTree(p.left,q.left)
        r2=self.isSameTree(p.right,q.right)

        if r1==True and r2==True:
            return True
        else:
            return False