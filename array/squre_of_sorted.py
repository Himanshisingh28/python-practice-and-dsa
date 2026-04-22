# You’re given a sorted array (ascending). Return a new array containing the squares of each number, also sorted in ascending order.
class Solution(object):
    def sortedSquares(self, nums):
        squre=[num**2 for num in nums]
        squre.sort()
        return squre
