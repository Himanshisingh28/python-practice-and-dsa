class Solution(object):
    def maxProduct(self, nums):
        i=0
        minending=nums[0]
        maxending=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            v1=minending*nums[i]
            v2=maxending*nums[i]
            v3=nums[i]
            maxending=max(v1,max(v2,v3))
            minending=min(v1,min(v2,v3))
            ans=max(ans,max(minending,maxending))
        return ans
        