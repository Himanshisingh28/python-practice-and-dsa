class Solution(object):
    def firstPosition(self,nums,target):
        res=-1
        low=0
        high=len(nums)-1
        while low<=high:
            guess=(low+high)//2
            if nums[guess]<target:
                low=guess+1
            elif nums[guess]>target:
                high=guess-1
            else:
                res=guess
                high = guess-1
        return res
    def seccondPosition(self,nums,target):
        res=-1
        low=0
        high=len(nums)-1
        while low<=high:
            guess=(low+high)//2
            if nums[guess]<target:
                low=guess+1
            elif nums[guess]>target:
                high=guess-1
            else:
                res=guess
                low=guess+1
        return res

    def searchRange(self, nums, target):
        return [self.firstPosition(nums,target),self.seccondPosition(nums,target)]
        