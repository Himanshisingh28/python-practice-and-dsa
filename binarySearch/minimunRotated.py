class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            guess=(low+high)//2
            if nums[guess]>nums[n-1]:
                low=guess+1
            else:
                res=guess
                high=guess-1
        return nums[res]

        
        