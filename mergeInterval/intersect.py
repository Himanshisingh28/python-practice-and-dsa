class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        i = 0
        j = 0
        res = []
        
        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            
            # Overlap check
            if end1 >= start2 and end2 >= start1:
                res.append([max(start1, start2), min(end1, end2)])
            
            # Move pointer
            if end1 < end2:
                i += 1
            else:
                j += 1
        
        return res