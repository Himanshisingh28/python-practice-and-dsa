from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        res = []
        q = deque([root])

        while q:
            lvlSize = len(q)
            temp = []

            for _ in range(lvlSize):
                node = q.popleft()
                temp.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(temp)

        return res