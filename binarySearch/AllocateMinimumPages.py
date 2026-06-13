class Solution:
    def helperFun(self, arr, limit, stud):
        k=1
        page=0
        for i in range (0,len(arr)):
            if page+arr[i]<=limit:
                page=page+arr[i]
            else:
                k+=1
                page=arr[i]
                if k>stud:
                    return False
        return True
    def findPages(self, arr, k):
        n=len(arr)
        if n<k:
            return -1
        low = max(arr)
        high = sum(arr)
        res=-1
        while low<=high:
            guess =(low+high)//2
            if self.helperFun(arr, guess, k):
                res = guess
                high = guess-1
            else:
                low=guess+1
        return res

