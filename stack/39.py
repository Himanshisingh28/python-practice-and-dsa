# this is question whaere we have to find the next greater element for each element in the array
# we can solve this problem using stack data structure
class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            if i < n and stack:
                res[i] = stack[-1]

            stack.append(nums[i % n])

        return res