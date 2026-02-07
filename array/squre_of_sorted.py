class Solution(object):
    def sortedSquares(self, nums):
        squre=[num**2 for num in nums]
        squre.sort()
        return squre