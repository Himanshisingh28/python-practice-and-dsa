
class Solution(object):
    def searchBST(self, root, val):
        
        if root is None:
            return 
        if root.val==val:
            return root
        if root.val<val:
           return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)