class Solution(object):
    def fourSum(self, nums, target):
        res=[]
        nums.sort()
        i=0
        n=len(nums)
        for i in range(0,n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                p=j+1
                q=n-1
                while p<q:
                    sum=nums[i]+nums[j]+nums[p]+nums[q]
                    if sum<target:
                        p+=1
                    elif sum>target:
                        q-=1
                    else:
                        res.append([nums[i],nums[j],nums[p],nums[q]])
                        p+=1
                        q-=1
                        while p<q and nums[p]==nums[p-1]:
                            p+=1

        return res
        