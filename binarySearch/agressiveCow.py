class Solution:
    def helperFun(self, stalls, k, guess):
        cows=1
        prevposition=stalls[0]
        for i in range(1,len(stalls)):
            distance=stalls[i]-prevposition
            if distance<guess:
                continue
            cows+=1
            prevposition = stalls[i]
        if cows>=k:
            return True
        else:
            return False
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n=len(stalls)
        low=1
        high=stalls[n-1]-stalls[0]
        res=-1
        while low<=high:
            guess=(low+high)//2
            if self.helperFun(stalls,k,guess):
                res=guess
                low=guess+1
            else:
                high=guess-1
        return res