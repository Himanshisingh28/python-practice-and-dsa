class Solution(object):
    def findMaxLength(self, nums):
        res=0
        zero=0
        one=0
        f={}
        n=len(nums)
        for i in range(0,n):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            diff=zero-one
            if diff==0:
                res=max(res,i+1)
                continue
            if diff not in f:
                f[diff]=i
            else:
                idx=f[diff]
                lenght=i-idx
                res=max(lenght,res)
        return res
        