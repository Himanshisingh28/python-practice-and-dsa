class Solution(object):
    def subarraysDivByK(self, nums, k):
        n=len(nums)
        ans=0
        sum=0
        f={0:1}
        res=0
        for i in range(0,n):
            sum+=nums[i]
            rem=sum%k
            if rem<0:
                rem=rem+k
            if rem in f:
                res += f[rem]

            f[rem] = f.get(rem, 0) + 1

        return res