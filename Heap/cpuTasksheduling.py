from collections import Counter 
class Solution(object):
    def leastInterval(self, tasks, n):
        freq=Counter(tasks)
        maxf=max(freq.values())
        lastrow=0
        for k,v in freq.items():
            if v==maxf:
                lastrow+=1
        return max(len(tasks),(maxf-1)*(n+1)+lastrow)
        