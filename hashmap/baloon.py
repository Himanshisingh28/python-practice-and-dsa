class Solution(object):
    def maxNumberOfBalloons(self, text):
        have={}
        need={
            'b':1,
            'a':1,
            'l':2,
            'o':2,
            'n':1
        }
        for ch in text:
            have[ch]=have.get(ch,0)+1

        res=float('inf')
        for ch in need:
            fneed=need[ch]
            fhave=have.get(ch,0)

            times=fhave//fneed

            res=min(res,times)
        return res
       