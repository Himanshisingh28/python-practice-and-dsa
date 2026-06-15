class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])
        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j]==target:
                    return True
        return False
class Solution(object):
    def searchMatrix(self, matrix, target):

        n=len(matrix)
        m=len(matrix[0])
        row=n-1
        col=0
        while row>=0 and col< m:
            if matrix[row][col]==target:
                return True
            if matrix[row][col]<target:
                col+=1
            else:
                row-=1
        return False
