class Solution(object):
    def minAbsoluteDifference(self, nums):
        last1=-1
        last2=-1
        ans=float('inf')

        for i in range(len(nums)):
            if nums[i]==1:
                last1=i
                if  last2!=-1:
                    diff=i-last2
                    if diff<ans:
                        ans=diff
                    
                    
            if nums[i]==2:
                last2=i
                if last1!=-1:
                    diff=i-last1
                    if diff<ans:
                        ans=diff
        if ans==float('inf'):
            return -1
        return ans
        