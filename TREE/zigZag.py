from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        res = []
        q = deque([root])
        leftToRight = True

        while q:
            levelSize = len(q)
            temp = [0] * levelSize

            for i in range(levelSize):
                node = q.popleft()

                if leftToRight:
                    index = i
                else:
                    index = levelSize - 1 - i

                temp[index] = node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(temp)
            leftToRight = not leftToRight

        return res