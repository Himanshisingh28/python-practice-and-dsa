class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total_sum = nums[0]
        max_ending = nums[0]
        min_ending = nums[0]
        max_sum = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            max_ending = max(num, max_ending + num)
            max_sum = max(max_sum, max_ending)

            min_ending = min(num, min_ending + num)
            min_sum = min(min_sum, min_ending)

            total_sum += num

        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)