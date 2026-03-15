def sahi(have, need):
    for c in need:
        if have.get(c,0) < need[c]:
            return False
    return True

class Solution(object):
    def minWindow(self, s, t):
        n=len(s)
        have={}
        need={}
        for c in t:
            need[c]=need.get(c,0)+1
        
        low=0
        res=float('inf')
        start=0


        for high in range(0,n):
            have[s[high]]=have.get(s[high],0)+1
            while sahi(have,need):
                l=high-low+1
                if res>l:
                    res=l
                    start=low
                have[s[low]]-=1
                low+=1
        if res == float('inf'):
            return ""
        
        return s[start:start+res] 