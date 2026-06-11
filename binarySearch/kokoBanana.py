class Solution(object):
    def findSpeed(self,piles,k):
        hour=0
        for i in range(0,len(piles)):
            hour=hour+piles[i]//k
            if piles[i]%k!=0:
                hour+=1
        return hour
    def minEatingSpeed(self, piles, h):
        n=len(piles)
        low=1
        high=max(piles)
        res=-1
        while low<=high:
            guess=(low+high)//2
            hour=self.findSpeed(piles,guess)
            if hour <= h:
                res = guess
                high = guess - 1
            else:
                low = guess + 1
        return res        