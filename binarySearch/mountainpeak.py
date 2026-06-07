class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)
        if n==1:
            return 0
        low=0
        high=n-1
        res=-1
        while low<high:
            guess=(low+high)//2
            if nums[guess]<nums[guess+1]:
                low=guess+1
            else:
                res=guess
                high=guess
        return low
        