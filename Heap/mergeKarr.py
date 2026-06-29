import heapq
class Node:
    def __init__(self,value,row,col):
        self.value=value
        self.row=row
        self.col=col

class Solution:
    def mergeArrays(self, mat):
        res=[]
        n=len(mat)
        m=len(mat[0])
        
        heap=[]
        
        for i in range(n):
            heapq.heappush(heap,(mat[i][0],i,0))
        while heap:
            value,row,col=heapq.heappop(heap)
            res.append(value)
            
            if col ==m-1:
                continue
            heapq.heappush(heap,(mat[row][col+1],row,col+1))
        return res
        