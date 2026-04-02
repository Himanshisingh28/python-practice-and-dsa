class Solution(object):
    def insert(self, intervals, newInterval):
        i=0
        res=[]
        insert=False
        for i in range(0,len(intervals)):
            if insert==False and intervals[i][0]>=newInterval[0]:
                res.append(newInterval)
                insert=True
            res.append(intervals[i])
        if insert==False:
            res.append(newInterval)
        merged = []
        for interval in res:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
            
        
        
        