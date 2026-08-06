class Solution(object):
    def houseRobber(self, nums, n, i, free, memo):
        if i == n:
            return 0

        if memo[i][free] != -1:
            return memo[i][free]

        if free == 0:
            memo[i][free] = self.houseRobber(nums, n, i + 1, 1, memo)
            return memo[i][free]

        c1 = nums[i] + self.houseRobber(nums, n, i + 1, 0, memo)
        c2 = self.houseRobber(nums, n, i + 1, 1, memo)

        memo[i][free] = max(c1, c2)
        return memo[i][free]

    def rob(self, nums):
        n = len(nums)
        memo = [[-1] * 2 for _ in range(n)]
        return self.houseRobber(nums, n, 0, 1, memo)