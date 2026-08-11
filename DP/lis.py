class Solution:
    def lengthOfLIS(self, nums):
        lis = []

        for x in nums:
            # Binary search
            low = 0
            high = len(lis)

            while low < high:
                mid = (low + high) // 2

                if lis[mid] < x:
                    low = mid + 1
                else:
                    high = mid

            # Replace or append
            if low == len(lis):
                lis.append(x)
            else:
                lis[low] = x

        return len(lis)