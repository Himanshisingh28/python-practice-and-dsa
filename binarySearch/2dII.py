class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        m=len(matrix[0])
        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j]==target:
                    return True
        return False