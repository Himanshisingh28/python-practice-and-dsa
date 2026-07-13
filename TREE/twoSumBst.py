from collections import deque

class Solution(object):

    def smallestNumber(self):
        if not self.asc:
            return None

        small = self.asc.pop()

        t = small.right
        while t:
            self.asc.append(t)
            t = t.left

        return small

    def largestNumber(self):
        if not self.dec:
            return None

        big = self.dec.pop()

        t = big.left
        while t:
            self.dec.append(t)
            t = t.right

        return big

    def findTarget(self, root, k):
        if root is None:
            return False

        self.asc = deque()
        self.dec = deque()

        t = root
        while t:
            self.asc.append(t)
            t = t.left

        t = root
        while t:
            self.dec.append(t)
            t = t.right

        i = self.smallestNumber()
        j = self.largestNumber()

        while i and j and i != j and i.val < j.val:

            currSum = i.val + j.val

            if currSum == k:
                return True

            elif currSum < k:
                i = self.smallestNumber()

            else:
                j = self.largestNumber()

        return False