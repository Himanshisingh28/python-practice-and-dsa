def find(a):
    if not a:
        return 0
    return max(a.values())
class Solution(object):
    def characterReplacement(self, s, k):
        low=0
        f={}
        n=len(s)
        high=0
        res=0
        for high in range(0,n):
            f[s[high]] = f.get(s[high],0) + 1 
            len1=high-low+1
            maxcount= find(f)
            diff=len1-maxcount
            while diff>k:
                f[s[low]]-=1
                low+=1
                maxcount=find(f)
                len1=high-low+1
                diff=len1-maxcount
            if diff<k or diff==k:
                len1=high-low+1
                res=max(res,len1)

        return res
