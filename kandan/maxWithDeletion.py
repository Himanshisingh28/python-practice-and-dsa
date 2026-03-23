class Solution(object):
    def maximumSum(self, arr):
        nodel=arr[0]
        onedel=float('-inf')
        res=arr[0]

        for i in range(1,len(arr)):
            prevNoDel=nodel

            nodel=max(arr[i],nodel+arr[i])
            onedel=max(prevNoDel,onedel+arr[i])
            res= max(res,nodel,onedel)
        return res